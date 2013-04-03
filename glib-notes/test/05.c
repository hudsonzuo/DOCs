#include <glib.h>
#include <glib/gprintf.h>

typedef struct _MySource MySource;
struct _MySource {
        GSource source;
        gchar text[256];
};

static gboolean
prepare (GSource *source, gint *timeout)
{
        MySource *mysource = (MySource *)source;
        g_print ("%s\n", mysource->text);
        *timeout = 0;
        
        return TRUE;
}

static gboolean
check (GSource *source)
{
        return TRUE;
}

static gboolean
dispatch (GSource *source, GSourceFunc callback, gpointer user_data)
{
        callback (user_data);
        
        return TRUE;
}

static void
finalize (GSource *source)
{
        g_print ("ha ha %d\n", source->ref_count);
}

struct _GMainLoop
{
  GMainContext *context;
  gboolean is_running;
  gint ref_count;
};

static gboolean
idle_func (gpointer data)
{
        return TRUE;
}

struct _GMainContext
{
#ifdef G_THREADS_ENABLED
  /* The following lock is used for both the list of sources
   * and the list of poll records
   */
  GStaticMutex mutex;
  GCond *cond;
  GThread *owner;
  guint owner_count;
  GSList *waiters;
#endif  

  gint ref_count;
};

int
main (void)
{
        GMainLoop *loop = g_main_loop_new (NULL, TRUE);
        g_print ("%d\n", loop->context->ref_count);
        GMainContext *context = g_main_loop_get_context (loop);
        g_print ("%d\n", context->ref_count);
        GSourceFuncs source_funcs = {prepare, check, dispatch, finalize};
        GSource *source = g_source_new (&source_funcs, sizeof(MySource));

        g_source_set_callback (source, idle_func, loop, NULL);
        
        g_source_attach (source, context);
        g_source_unref (source);
        
        g_print ("%d\n", context->ref_count);
        g_main_loop_run (loop);

        g_main_context_unref (context);

                g_print ("%d\n", context->ref_count);
        
        g_main_loop_unref (loop);
        
        g_print ("%d\n", context->ref_count);
        
        return 0;
}
