#!/usr/bin/python2.6
import sys
from  divide_small import *
class JIU:
   def __init__(self,primeValue):
      #JIU_len_maybe=divide_small.divide_small(primeValue-1).get()
      JIU_len_maybe=[486,236682,115264134]
      self.JIU_len=-1
      for Try in JIU_len_maybe:
         yu=make_I(Try)%primeValue
	 print Try,yu
         if yu == 0:
            self.JIU_len=Try
            break
   def get(self):
      return self.JIU_len


def make_I(len_I):
   len_100=1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
   len_100_0=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
   len_10=1111111111
   I=0
   do_100=len_I/100
   do_left=len_I%100
   while do_100 > 0:
      I=I*len_100_0+len_100
      do_100=do_100-1
   do_10=do_left/10
   do_1=do_left%10
   while do_10 > 0:
      I=I*10000000000+len_10
      do_10=do_10-1
   while do_1 > 0:
      I=I*10+1
      do_1=do_1-1
   return I   
if __name__ == "__main__":
   re=JIU(int(sys.argv[1])).get()
   if re != -1:
      print sys.argv[1],' : ',re,':::',divide_small(int(sys.argv[1])).get()
