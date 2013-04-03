#include <gio/gio.h>
 
static void
dir_is_changed (GFileMonitor *monitor,
                GFile *file,
                GFile *other,
                GFileMonitorEvent event_type,
                gpointer user_data)
{
        if (event_type == G_FILE_MONITOR_EVENT_CREATED)
                g_print ("You just created '%s'!\n", g_file_get_path (file));
}
 
int
main (int argc, char **argv)
{
        g_type_init ();
 
        GMainLoop *main_loop = g_main_loop_new (NULL, TRUE);
         
         
        GFile *file = g_file_new_for_path ("/tmp/cikada");
        GFileMonitor * monitor = g_file_monitor_directory (file,
                                                           G_FILE_MONITOR_NONE,
                                                           NULL,
                                                           NULL);
 
        g_signal_connect (monitor, "changed", (GCallback)dir_is_changed, NULL);
 
        g_main_loop_run (main_loop);
 
        g_object_unref (file);
        g_main_loop_unref (main_loop);
         
        return 0;
}