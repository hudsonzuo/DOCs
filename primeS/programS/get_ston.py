#!/usr/bin/python2.6
import sys
import fenJie
from math import sqrt,floor
from multiprocessing import Process,Manager,cpu_count
from io import FileIO
from time import sleep,time
from divide_small import *
class stone:
   def __init__(self,jiu_len=6):
   #   print 'stone come for:',jiu_len
      factor_jiu_len=divide_small(jiu_len).get()
      self.stone_this=make_I(jiu_len)
      if len(factor_jiu_len) > 0:
         for fac in factor_jiu_len:
            self.stone_this=self.stone_this/stone(jiu_len=fac).get_stone()
   def get_stone(self):	 
      return self.stone_this
	    
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
   if len(sys.argv) == 2:
      st_this=stone(int(sys.argv[1]))
      print st_this.get_stone()
   elif len(sys.argv) == 3:
      start=int(sys.argv[1])
      while start < int(sys.argv[2]):
         st_this=stone(start)
         print start,':',st_this.get_stone()
         del st_this
         start=start+1
   else:
      print ""
      print './get_stone.py num'
      print 'or ./get_stone.py min max'
      quit()
      
