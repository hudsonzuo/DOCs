#include <glib.h>

#define NUMBER_OF_THREADS 4

typedef struct _MyData MyData;
struct _MyData {
        GThreadPool *thread_pool;
        GAsyncQueue *queue;
};

static void
send_message (gpointer data, gpointer user_data)
{
        
        MyData *p = (MyData *)data;
        gchar *buffer = (gchar *)g_async_queue_pop (p->queue);
        g_usleep (5 * G_USEC_PER_SEC);
        g_print (">>>> OK! I got %s", buffer);
        g_free (buffer);
}

gboolean
io_watch (GIOChannel *channel, GIOCondition condition, gpointer data)
{
        MyData *p = (MyData *)data;
        gchar *buffer;

        g_thread_pool_push (p->thread_pool, data, NULL);
        
        g_io_channel_read_line (channel, &buffer, NULL, NULL, NULL);        
        g_async_queue_push (p->queue, buffer);

        return TRUE;
}

int
main (void)
{       
#if defined(G_THREADS_ENABLED) && !defined(G_THREADS_IMPL_NONE)
        g_thread_init (NULL);
        
        MyData data;
        data.thread_pool = g_thread_pool_new (send_message,
                                                NULL,
                                                NUMBER_OF_THREADS,
                                                FALSE,
                                                NULL);
        data.queue = g_async_queue_new ();
        GMainLoop *loop = g_main_loop_new (NULL, FALSE);
        GIOChannel* channel = g_io_channel_unix_new (1);
        if (channel){
                g_io_add_watch(channel, G_IO_IN, io_watch, &data);
                g_io_channel_unref(channel);
        }
        
        g_main_loop_run(loop);
        g_main_context_unref (g_main_loop_get_context (loop));
        g_main_loop_unref(loop);
        
        g_thread_pool_free (data.thread_pool, TRUE, TRUE);
        g_async_queue_unref (data.queue);
#endif
        return 0;
}
