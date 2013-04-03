#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
  int ccc=0;
  int idx=0;
  printf ("size of char is %d \n",sizeof(char));
  for(ccc=1; ;ccc++)
   {
        if(ccc < idx) break;
	printf(" %u   ",ccc);
        idx=ccc;
   }
  return 0;

}
