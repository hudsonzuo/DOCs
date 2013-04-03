#!/usr/bin/python3
# -*- encoding:utf-8 -*
import sys
from optparse import OptionParser
from multiprocessing import Process,Queue, Manager
import time
from math import pow
from io import FileIO
from cmd import *
import re
class spyYU(Cmd):
   prompt='YU > '
   def do_init(self,primeValue):
      self.primeValue=int(primeValue)
      self.f_log=FileIO('./log/spyYu.log','a')
      self.JIU_len=1
      self.mainYU=[]
      yy=10 % self.primeValue
      self.mainYU.append(yy)
      self.SH=10/self.primeValue
      while self.mainYU[-1] != 1:
         self.SH=self.SH*10+(self.mainYU[-1]*10)/self.primeValue
         yy=self.mainYU[-1]*10%self.primeValue
         self.mainYU.append(yy)
         self.JIU_len = self.JIU_len+1
      print self.mainYU   
   def do_get_len(self,line):   
      print self.JIU_len
   def do_get_SH(self,line):
      print self.SH 
   def get_YU(self,yu):
      YU=[]
      for yy in self.mainYU:
         yy=yy*yu%self.primeValue
         YU.append(yy)
      return  YU   
   def do_get_YU(self,yu):  # 余环用其中的一个余数（一般是最小值）代表，本方法是根据代表余数求取余环
      if yu == '':
         yu=1
      print self.YU_sort(self.get_YU(int(yu)))
   def get_key(self,YU):  #获取余环的代表余数(最小值）
      YU_key=int(YU[0])
      for yy in YU:
         if int(yy) < YU_key:
            YU_key=int(yy)
      return YU_key      
   def do_get_key(self,line):  #获取余环的代表余数(最小值）
      if line=='':
         print 'get_key 余环'
      else:   
         YU_str=re.sub('\]','',re.sub('\[','',re.sub('L','',line)))
         YU=re.split(', ',YU_str)
         print self.get_key(YU)

   def multi(self,keys): #余环的乘法运算
      multi=int(keys[0])
      for key in keys[1:]:
         multi=multi*int(key)%self.primeValue
      return multi
   def do_multi(self,line): #余环的乘法运算
      keys=re.split(' ',line)
      self.do_get_YU(str(self.multi(keys)))
   def YU_sort(self,YU):
      key=self.get_key(YU)
      idx=YU.index(key)
      result=[]
      result.extend(YU[idx:])
      result.extend(YU[:idx])
      return result
   def do_EOF(self, line):
      "Exit"
      return True
   def do_power(self,line):
      paras=re.split(' ',line)
      key=int(paras[0])
      power=int(paras[1])
      keys=[]
      while power > 0:
         keys.append(key)
         power=power-1
      self.do_get_YU(str(self.multi(keys)))
      

if __name__ == "__main__":
   spyYU().cmdloop('余环探索')


