#!/usr/bin/python2.6

import sys
from optparse import OptionParser
from multiprocessing import Process,Queue, Manager
import time
class JIU:
   def cal_yu(self,prime,yuList):
      yu=-1
      while True:
        yu=(yuList[-1]*10)%prime.value
        if yu != 1:
           yuList.append(yu)
        else:
           break
   def cal_sh(self,prime,yuList,SH):
      idx=0
      while True:
   #     print yuList
        if len(yuList) < idx+2:
          time.sleep(3)
          if len(yuList) < idx+2:
   	     break
        sh=(yuList[idx]*10-yuList[idx+1])/prime.value
        idx=idx+1
        SH.value=SH.value*10+sh
      sh=(yuList[idx]*10-yuList[0])/prime.value
      SH.value=SH.value*10+sh
        
      if yuList[-1]*10%prime.value != 1:
         print 'cal_sh() is based on incorrect yuList'
   def __init__(self,primeValue):
      manager=Manager()   
      self.JIU_len=0
      prime=manager.Value('L',int(primeValue))
      self.yuList=manager.list([1])
      self.SH=manager.Value('L',0)
      p_yu = Process(target = self.cal_yu, args = [prime,self.yuList])
      p_yu.start()
      p_sh = Process(target = self.cal_sh, args = [prime,self.yuList,self.SH])
      p_sh.start()
      p_yu.join()
      p_sh.join()
      self.JIU_len=len(self.yuList)
      self.treeYu=list(self.yuList)
      for car in range(2,int(primeValue)):
         if self.treeYu.count(car) >0:
            continue
	 else:
	    newList=[]
	    for yy in self.yuList:
               newList.append(yy*car%int(primeValue))
	    self.treeYu.append(';')   
            self.treeYu=self.treeYu+newList
   def get_JIU_len(self):   
      return self.JIU_len
   def get_JIU_SH(self):
      return self.SH.value
   def get_JIU_yu(self):
      return self.yuList
   def get_treeYu(self):
      return self.treeYu
if __name__ == "__main__":
   if len(sys.argv) == 1:
      print 'I need a number,often a prime number to give you its JIU'
      quit()
   if len(sys.argv) > 1:
      jiu_this=JIU(sys.argv[1])
      print jiu_this.get_JIU_len()
      print jiu_this.get_JIU_SH()
      print jiu_this.get_JIU_yu()
      #print jiu_this.get_treeYu()
