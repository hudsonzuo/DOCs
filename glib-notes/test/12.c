#include <glib.h>

struct mutex_int_t {
        GMutex *mutex;
        gint i;
};

static gpointer
thread_1 (gpointer data)
{
        struct mutex_int_t * p = (struct mutex_int_t *)data;

        if (!g_mutex_trylock (p->mutex))
                g_thread_exit (NULL);
        
        for (int i = 0; i < 4; i++){
                p->i++;
                g_print ("thread_1 said %d\n", p->i);
        }
        g_mutex_unlock (p->mutex);
        
        return NULL;
}

static gpointer
thread_2 (gpointer data)
{
        struct mutex_int_t * p = (struct mutex_int_t *)data;

        g_mutex_lock (p->mutex);
        for (int i = 0; i < 4; i++){
                p->i++;
                g_print ("thread_2 said %d\n", p->i);
        }
        g_mutex_unlock (p->mutex);
        
        return NULL;
}

int
main (void)
{
#if defined(G_THREADS_ENABLED) && !defined(G_THREADS_IMPL_NONE)
        g_thread_init (NULL);

        struct mutex_int_t i = {g_mutex_new (), 0};
        
        GThread *t1 = g_thread_create (thread_1, &i, TRUE, NULL);
        GThread *t2 = g_thread_create (thread_2, &i, TRUE, NULL);

        g_thread_join (t1);
        g_thread_join (t2);
#endif
        return 0;
}
