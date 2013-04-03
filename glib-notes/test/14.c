#include <glib.h>

#define NUMBER_OF_THREADS 4

typedef struct _MyData MyData;
struct _MyData {
        GThreadPool *thread_pool;
        gchar *buffer;
};

static void
send_message (gpointer data, gpointer user_data)
{
        g_usleep (5 * G_USEC_PER_SEC);
        g_print (">>>> OK! I got %s", (gchar *)data);
        g_free (data);
}

gboolean
io_watch (GIOChannel *channel, GIOCondition condition, gpointer data)
{
        static gint count = 0;
        MyData *mydata = (MyData *)data;
        
        g_io_channel_read_line (channel, &(mydata->buffer), NULL, NULL, NULL);
        g_thread_pool_push (mydata->thread_pool, mydata->buffer, NULL);
        
        return TRUE;
}

int
main (void)
{       
#if defined(G_THREADS_ENABLED) && !defined(G_THREADS_IMPL_NONE)
        g_thread_init (NULL);
        
        MyData mydata = {NULL, NULL};
        mydata.thread_pool = g_thread_pool_new (send_message,
                                                NULL,
                                                NUMBER_OF_THREADS,
                                                FALSE,
                                                NULL);
        
        GMainLoop *loop = g_main_loop_new (NULL, FALSE);
        GIOChannel* channel = g_io_channel_unix_new (1);
        if (channel){
                g_io_add_watch(channel, G_IO_IN, io_watch, &mydata);
                g_io_channel_unref(channel);
        }
        
        g_main_loop_run(loop);
        g_main_context_unref (g_main_loop_get_context (loop));
        g_main_loop_unref(loop);
        
        g_thread_pool_free (mydata.thread_pool, TRUE, TRUE);
#endif
        return 0;
}
