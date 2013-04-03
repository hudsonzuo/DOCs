#include <glib.h>

int main()
{
        gchar *s = "hello world!";
        gintptr p = (gintptr)s;
        g_print ("%#" G_GINTPTR_MODIFIER "x\n", p);
        g_print ("%" G_GINTPTR_FORMAT "\n", p);
        
        return 0;
}

