#include <glib.h>

gboolean
mystatus (gpointer data)
{
        GMainLoop *event_loop = data;
        static guint count = 10;
        
        if(--count == 0){
                g_print("I am dead!\n");
                g_main_loop_quit (event_loop);
                return FALSE;
        }
        g_print ("I am here!\n");
        
        return TRUE;
}

int
main (void)
{
        if (g_thread_get_initialized ())
                g_print ("ha ha\n");
        GMainLoop *main_loop = g_main_loop_new (NULL, TRUE);

        g_timeout_add(100, mystatus, main_loop);
        g_main_loop_run (main_loop);
        
        g_main_loop_unref(main_loop);
        
        return 0;
}

        
        
