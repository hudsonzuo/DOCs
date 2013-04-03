#include <glib.h>

int
main (void)
{
        GFloatIEEE754 a = {3.1415};
        g_print ("%u\n", a.mpn.sign);
        g_print ("%u\n", a.mpn.biased_exponent);
        g_print ("%u\n", a.mpn.mantissa);

        
}
