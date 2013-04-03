#include <glib.h>

static gboolean
timeout_func (gpointer data)
{
        static guint i = 0;
        i += 2;
        g_print ("%d\n", i);
        
        return TRUE;
}

int
main (void)
{
        GMainLoop *loop = g_main_loop_new (NULL, TRUE);
        GMainContext *context = g_main_loop_get_context (loop);
        
                g_timeout_add (10000, timeout_func, loop);
        g_main_loop_run (loop);
        
        g_main_context_unref (context);
        g_main_loop_unref (loop);
        
        return 0;
}

