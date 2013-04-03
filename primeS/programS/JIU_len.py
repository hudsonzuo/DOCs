#!/usr/bin/python2.6

import sys
import time
from make_jiu import make_jiu
class JIU_len:
   def __init__(self,primeValue):
      li_yu_head=[]
      jiu_this=9
      self.JIU_len=0 
      while jiu_this<=int(make_jiu(10)):
         li_yu_head.append(jiu_this%primeValue)
         jiu_this=jiu_this*10+9
      if li_yu_head.count(li_yu_head[-1]) >1 :
         self.JIU_len=li_yu_head.index(0)+1
         #print 'it is a small figure:'
         #print li_yu_head
         return 
      self.JIU_len=10  
      #print li_yu_head
      yy=li_yu_head[-1]
      while True:
         yy=(yy*pow(10,10)+make_jiu(10))%primeValue
         #print yy
         #time.sleep(1)
         if li_yu_head.count(yy)>0:
            self.JIU_len=self.JIU_len+10-li_yu_head.index(yy)-1
            break
         else:
            self.JIU_len=self.JIU_len+10
   def result(self):   
      return self.JIU_len
if __name__ == "__main__":
   if len(sys.argv) == 1:
      print 'I need a number,often a prime number to give you its JIU'
      quit()
   if len(sys.argv) > 1:
      jiu_this=JIU_len(int(sys.argv[1]))
      print jiu_this.result()
      #print jiu_this.get_treeYu()
