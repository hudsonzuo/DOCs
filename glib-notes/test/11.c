#include <glib.h>

static gpointer
func_1 (gpointer data)
{
        for (int i = 0; i < 3; i++)
                g_print ("I'm func_1\n");
        
        return NULL;
}

static gpointer
func_2 (gpointer data)
{
        for (int i = 0; i < 3; i++)
                g_print ("I'm func_2\n");
        
        return NULL;
}

int
main (void)
{
#if defined(G_THREADS_ENABLED) && !defined(G_THREADS_IMPL_NONE)
        g_thread_init (NULL);
        
        g_thread_create (func_1, NULL, TRUE, NULL);
        g_thread_create (func_2, NULL, TRUE, NULL);
        
        for (int i = 0; i < 3; i++)
                g_print ("I'm main thread\n");
#endif
        return 0;
}

