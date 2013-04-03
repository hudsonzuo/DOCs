#!/usr/bin/python
import sys
import fenJie
from math import sqrt,floor
from multiprocessing import Process,Manager,cpu_count
from io import FileIO
from time import sleep,time
class stone:
   def __init__(self,jiu_len=6,roof=99999999999999999999):
#      print 'stone come for:',jiu_len
      factor_jiu_len=factor(jiu_len)
      self.stone_this=make_I(jiu_len)
      if len(factor_jiu_len) > 0:
         for fac in factor_jiu_len:
            self.stone_this=self.stone_this/stone(jiu_len=fac).get_stone()
      jiu_len_tmp=jiu_len
      while jiu_len_tmp%3==0:
         self.stone_this=self.stone_this/3
         jiu_len_tmp=jiu_len_tmp/3
      
      self.jiu_len=jiu_len
      self.stone_factor=[]
      self.roof=roof
   def get_stone(self):	 
      return self.stone_this
   def get_stone_factor(self):
      return self.stone_factor
   def stone_prime(self,stone_now):
      A0=stone_now-1
      L=A0%self.jiu_len
      Q=(A0-L)/self.jiu_len
      for t_try in range(0,Q):
         M=(L+t_try*self.jiu_len)^2-4*(Q-t_try)
         M_sqrt=sqrt(M)
         if floor(M_sqrt) < M_sqrt:
            break;
         elif L+t_try*self.jiu_len+M)%2 == 0:
            X1=(L+t_try*self.jiu_len-M)/2
            X2=(L+t_try*self.jiu_len+M)/2
            print 'Got a pair of X:',X1,X2
            self.stone_factor.append(X1*self.jiu_len+1)
            self.stone_prime(X2*self.jiu_len+1)
            break
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
     
     
def factor(num):
   li_factor=[]
   ii=1
   for ii in range(2,num-1):
      if num % ii == 0:
         li_factor.append(ii)
   return li_factor
