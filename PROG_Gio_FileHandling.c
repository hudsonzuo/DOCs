#include <glib/gprintf.h>
#include <gio/gio.h>
 
#define _g_free0(var) (var = (g_free (var), NULL))
#define _g_object_unref0(var) ((var == NULL) ? NULL : (var = (g_object_unref (var), NULL)))
 
void log_g_error(GError * e, int line) {
   g_printerr ("** ERROR **: %s (domain: %s, code: %d) at %d\n", 
      e->message, g_quark_to_string (e->domain), e->code, line);
}
 
int main (int argc, char ** argv) {
   g_type_init ();
   if (argc < 2) {
      g_message ("Usage: %s file-name", argv[0]);
      return 1;
   }
   GFile* file = NULL;
   GFileInfo* fileinfo = NULL;
   GFileType filetype = G_FILE_TYPE_UNKNOWN;
   const char* contenttype = NULL;
   gchar* contenttype_desc = NULL;
   GFileInputStream* fis = NULL;
   GDataInputStream* dis = NULL;
   gchar* line = NULL;
   GError* inner_error = NULL;
   int error_line = 0;
   file = g_file_new_for_path (argv[1]);
   fileinfo = g_file_query_info (file, "standard::*", G_FILE_QUERY_INFO_NONE, NULL, &inner_error);
   if (inner_error == NULL) {
      filetype = g_file_info_get_file_type(fileinfo);
      contenttype = g_file_info_get_attribute_string (fileinfo, G_FILE_ATTRIBUTE_STANDARD_CONTENT_TYPE);
      contenttype_desc = g_content_type_get_description(contenttype);
      g_printf ("\
=== file-description ===\n\
Content type: %s (%s)\n\
Size: %lluB\n\
=== description-end ===\n\
", contenttype, contenttype_desc, g_file_info_get_attribute_uint64 (fileinfo, G_FILE_ATTRIBUTE_STANDARD_SIZE));
      _g_free0 (contenttype_desc);
      //_g_object_unref0 (fileinfo); //if you do this here, 'contenttype' gets destroyed.
      switch (filetype) {
      case G_FILE_TYPE_REGULAR:
      case G_FILE_TYPE_SYMBOLIC_LINK:
         if (!g_content_type_is_a(contenttype, "text/*")) {
            g_printerr ("Not a text-based document.\n");
      break;
         }
         fis = g_file_read (file, NULL, &inner_error);
         if (inner_error != NULL) {
            _g_object_unref0 (fis);
            error_line = __LINE__;
      break;
         }
         dis = g_data_input_stream_new (G_INPUT_STREAM(fis));
         _g_object_unref0 (fis);
         while (TRUE) {
            line = g_data_input_stream_read_line (dis, NULL, NULL, &inner_error);
            if (inner_error != NULL) {
               _g_free0 (line);
               error_line = __LINE__;
         break;
            }
            if (line == NULL)
         break;
            g_printf ("%s\n", line);
            _g_free0 (line);
         }
         _g_object_unref0 (dis);
      break;
      case G_FILE_TYPE_DIRECTORY:
         g_printerr ("** INFO: Can't read a directory.\n");
      break;
      case G_FILE_TYPE_SPECIAL:
         g_printerr ("** INFO: It's a \"special\" file.\n");
      break;
      case G_FILE_TYPE_SHORTCUT:
         g_printerr ("** INFO: The given file is a shortcut.\n");
      break;
      case G_FILE_TYPE_MOUNTABLE:
         g_printerr ("** INFO: File is a mountable location.\n");
      break;
      case G_FILE_TYPE_UNKNOWN:
         g_printerr ("** INFO: Unknown file type.\n");
      break;
      }
   }
 
   _g_object_unref0 (fileinfo);
   _g_object_unref0 (file);
   if (inner_error != NULL) {
      log_g_error (inner_error, error_line);
      g_clear_error (&inner_error);
      return 1;
   }
   return 0;
}