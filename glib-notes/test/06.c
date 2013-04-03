#include <glib.h>

static gboolean
idle_func (gpointer data)
{
        g_print ("Just once!\n");
        g_main_loop_quit (data);
        
        return TRUE;
}

int
main (void)
{
        GMainLoop *loop = g_main_loop_new (NULL, TRUE);
        
        g_idle_add (idle_func, loop);
        g_main_loop_run (loop);
        
        g_main_loop_unref (loop);
        
        return 0;
}
