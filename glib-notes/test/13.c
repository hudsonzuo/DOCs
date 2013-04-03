#include <glib.h>

GCond* data_cond = NULL;
GMutex* data_mutex = NULL;
gpointer current_data = NULL;
gchar *buffer = NULL;

static void
consumer_1 (void)
{
        g_mutex_lock (data_mutex);
        while (!buffer)
                g_cond_wait (data_cond, data_mutex);
        g_print ("%ld\n", g_utf8_strlen (buffer, -1) - 1);
        g_mutex_unlock (data_mutex);
}

static void
consumer_2 (void)
{
        g_mutex_lock (data_mutex);
        while (!buffer)
                g_cond_wait (data_cond, data_mutex);
        for (int i = g_utf8_strlen (buffer, -1) - 2; i >= 0; i--)
                g_print ("%c", buffer[i]);
        g_print ("\n");
        g_mutex_unlock (data_mutex);
}

gboolean
io_watch (GIOChannel *channel, GIOCondition condition, gpointer data)
{       
        g_mutex_lock (data_mutex);
        g_io_channel_read_line (channel, &buffer, NULL, NULL, NULL);
        g_cond_signal (data_cond);
        g_mutex_unlock (data_mutex);

        GThread *consumer_thread_1 =
                g_thread_create ((GThreadFunc)consumer_1, NULL, TRUE, NULL);
        GThread *consumer_thread_2 =
                g_thread_create ((GThreadFunc)consumer_2, NULL, TRUE, NULL);
        
        g_thread_join (consumer_thread_1);
        g_thread_join (consumer_thread_2);
        
        g_free (buffer);
        buffer = NULL;
        
        return TRUE;
}

int
main (void)
{
#if defined(G_THREADS_ENABLED) && !defined(G_THREADS_IMPL_NONE)
        g_thread_init (NULL);
        
        data_cond = g_cond_new ();
        data_mutex = g_mutex_new ();
        
        GMainLoop *loop = g_main_loop_new (NULL, FALSE);
        GIOChannel* channel = g_io_channel_unix_new (1);
        if (channel){
                g_io_add_watch(channel, G_IO_IN, io_watch, NULL);
                g_io_channel_unref(channel);
        }
        g_main_loop_run(loop);
        g_main_context_unref (g_main_loop_get_context (loop));
        g_main_loop_unref(loop);
        
        g_mutex_free (data_mutex);
        g_cond_free (data_cond);
#endif
        return 0;
}
