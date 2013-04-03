#!/usr/bin/python2.6

import sys
from optparse import OptionParser
from multiprocessing import Process,Queue, Manager
import time
from math import pow
from io import FileIO

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
   def treeYu_find(self,num):
      result=None
      for oneYu in self.treeYu:
         if oneYu[2].count(num) > 0:
            result=oneYu
            break
      return result   
   def __init__(self,primeValue):
      self.f_log=FileIO('./log/treeYu.log','a')
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
      self.treeYu=[]
      self.X=(int(primeValue)-1)/self.JIU_len
      self.X_dimension=self.factor_X(self.X)
      self.f_log.write('X='+str(self.X)+','+str(self.X_dimension)+'\n')
      for car in range(1,int(primeValue)):
         if self.treeYu_find(car) != None:
            continue
         else:
	    oneYu_member=[]
	    for yy in self.yuList:
               oneYu_member.append(yy*car%int(primeValue))
            oneYu=[]   
            oneYu.append(car)
            oneYu_coor=dict()
            for dim in self.X_dimension.keys():
               oneYu_coor[dim]=-1
            oneYu.append(oneYu_coor)
            oneYu.append(oneYu_member)
            self.f_log.write(str(oneYu)+'\n')
      	    #self.treeYu.append(oneYu)   
      self.primeValue=int(primeValue)
   def get_JIU_len(self):   
      return self.JIU_len
   def get_JIU_SH(self):
      return self.SH.value
   def get_JIU_yu(self):
      return self.yuList
   def get_treeYu(self):
      self.treeYu.sort()
      return self.treeYu
   def Yu_next(self,oneYu,dimen):
      car_next=pow(oneYu[0],dimen)%self.primeValue
      return self.treeYu_find(car_next)
   #   ---@---@---@---@---@---@
   #              |___________|

   def process_TreeYu_coordinate(self):
      for oneYu in self.treeYu:
         stack=[]
         stack.append(oneYu)
         for dimen in self.X_dimension.keys():
            if oneYu[1][dimen] >=0:
               break
            Yu_this=oneYu
            for dimen_multi in range(1,self.X_dimension[dimen]+1):
               Yu_this=self.Yu_next(Yu_this,dimen)
               #print '99999999',Yu_this
               if stack.count(Yu_this) > 0:
                  #print '1111111111111'
                  stack.append(Yu_this)
                  break
               else:
                  stack.append(Yu_this)
            multi_point=stack.index(stack[-1])
            #print 'multi_point=',multi_point
            #print 'stack:',stack      
            for dimen_multi in range(0,multi_point):   # peocess those on line
               stack[dimen_multi][1][dimen]=self.X_dimension[dimen]-dimen_multi
            for dimen_multi in range(multi_point+1,len(stack)): # process those on circle
               stack[dimen_multi][1][dimen]=0
            

       
   def factor_X(self,X):
     # result=[]
     # result_factor=[]
      result_multi=dict()
      BY=X
      for Try in range(2,BY):
         onefactor_multi=0
         while BY%Try==0:
            onefactor_multi=onefactor_multi+1
            BY=BY/Try
         if onefactor_multi >0:
            #result_factor.append(Try)
            result_multi[Try]=onefactor_multi
         if BY == 1:
            break
      #result.append(result_factor)
      #result.append(result_multi)
      if len(result_multi)==0:
         result_multi[X]=1
      return result_multi
if __name__ == "__main__":
   if len(sys.argv) == 1:
      print 'I need a number,often a prime number to give you its JIU'
      quit()
   if len(sys.argv) > 1:
      jiu_this=JIU(sys.argv[1])
      print jiu_this.get_JIU_len()
      print jiu_this.get_JIU_SH()
      print jiu_this.get_JIU_yu()
      #jiu_this.process_TreeYu_coordinate()
      #for oneYu in  jiu_this.get_treeYu():
      #   print oneYu

