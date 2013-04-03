#!/usr/bin/python2.6
# -*- encoding:utf-8 -*
import sys
import psyco
from math import sqrt,floor
from multiprocessing import Process,Manager,cpu_count
from io import FileIO
from time import sleep,time
from divide_small import divide_small
class stone:
   def __init__(self,jiu_len=6,roof=99999999999999999999):
#      print 'stone come for:',jiu_len
      self.stone_factor=[]
      self.stone=make_I(jiu_len)
      self.jiu_len=jiu_len
      self.Wait = 1*0.1
      if jiu_len ==1:
         self.stone_factor.append(3)
         return
      self.f_log=FileIO('./log/stone_son.log','a')
      self.f_log.write('=======================================================================================\n')
      self.f_log.write('start working on stone for'+str(jiu_len)+'\n')
      factor_jiu_len=divide_small(jiu_len)
      
      #if len(factor_jiu_len) > 0:
      for fac in factor_jiu_len.get():
         self.stone=self.stone/stone(jiu_len=fac).get_stone()
      
      self.roof=roof
      self.jiu_len=jiu_len
      self.stone_this =self.stone
      for beTry in factor_jiu_len.get_full():      #本征幂余, V整除jiu_len
         if self.stone_this % beTry ==0:
            self.stone_factor.append(beTry)
            self.stone_this=self.stone_this/beTry
      if (len(str(self.stone_this)) > 17):
         self.Wait=(len(str(self.stone_this))-17)*0.1
      if (self.Wait > 60):
         self.Wait=60
   def get_stone(self):         
      return self.stone
   def get_stone_factor(self):
      return self.stone_factor
   def stone_prime_sub(self,st,factors,env):
      #print st,env
      has_prime_flag=False
      beTry=env['start']
      while beTry < env['end']:
         if st%beTry == 0:
            has_prime_flag=True
            factors.append(beTry)
            self.f_log.write('find a factor(maybe a prime):'+str(beTry)+' for '+str(st)+'\n')
         elif beTry >self.roof:
            self.f_log.write('over roof:'+str(beTry)+'\n')
            return []
         beTry=beTry+env['step']
         #self.f_log.write(str(beTry)+'\n'+str(env['end'])+'\n')
      if has_prime_flag == False and st < self.stone_this:
         factors.append(st)
      elif has_prime_flag == False and st==self.stone_this and env['step']==self.jiu_len:
         factors.append(st)
      return factors               
   def stone_prime_start(self):
      if self.jiu_len > 1:
        self.stone_prime_master(self.stone_this)
   def stone_prime_master(self,stone_now):
      jiu_len=self.jiu_len
      manager=Manager()
      factor_list=manager.list([])
      env=dict()
      p_sub=[]
      cpuCount=cpu_count()
      #S=11111111111111111,jiu_len=17, 17x偶数+1
      #S=100000001,jiu_len=16, 16x正整数+1
      #
      stone_prime_sub_quick=psyco.proxy(self.stone_prime_sub)
      for idx_cpu in range(0, cpuCount/4):
         for helper in range(0,5):
            if jiu_len%2 == 0:
               env['step']=jiu_len*5*cpuCount/4
               env['start']=jiu_len+1+jiu_len*(helper%5)+jiu_len*5*idx_cpu
            else:
               env['step']=jiu_len*10*cpuCount/4
               env['start']=jiu_len*2+1+jiu_len*2*(helper%5)+jiu_len*10*idx_cpu
            if env['start']%10 == 5:
               self.f_log.write('divisor watching:'+str(idx_cpu)+','+str(helper)+',,,,'+str(env['start'])+'\n')
               continue
            #env['end']=int(sqrt(stone_now))+1
            len_stone=len(str(stone_now))
            if len_stone%2 == 0:
               env['end']=make_I(len_stone/2)*9+1  #stone<九_L<10^L => sqrt(stone)<10^((L+1)/2)=make_I((L+1)/2)*9 L是奇数, 
            else:                                  #               或者=>sqrt(stone)<10(L/2)=make_I(L/2)*9 L是偶数
               env['end']=make_I((len_stone+1)/2)*9+1
            if env['end']*env['end']<stone_now:
               print 'end error: end=',env['end'],'stone=',stone_now
            env['step_usual']=env['step']/(5*cpuCount/4)
            self.f_log.write('before sub:'+str(stone_now)+'  '+str(env)+'\n')
            p_sub.append(Process(target = stone_prime_sub_quick, args = [stone_now,factor_list,env]))
            p_sub[-1].start()
      
      turnOut=False
      while True:
         alive_sub=False
         for sub in p_sub:
           if sub.is_alive():
               alive_sub=True
               break
         prime_total=1
         if len(factor_list) >0:
            #print factor_list,stone_now
            for sub in p_sub:
                if sub.is_alive():
                   sub.terminate()
            factor_list.sort()
            factor_list_new=[]
            factor_list_new.append(factor_list[0])
            for fa in factor_list:
               if fa != factor_list_new[-1]:
                  factor_list_new.append(fa)
            for fa in factor_list_new:
                is_prime=True
                for prime in self.stone_factor:
                    if fa%prime==0 and fa > prime:
                        is_prime=False
                if is_prime == True:
                    self.stone_factor.append(fa)
                    self.stone_factor.sort()
            factor_list=[]
            stone_now=self.stone
            for fa in self.stone_factor: 
               stone_now=stone_now/fa
            if stone_now >1 :
               self.f_log.write('a new stone master come up,'+str(stone_now)+','+str(self.stone_factor)+'\n')
               self.stone_prime_master(stone_now)
               break
            else:
               return factor_list_new
         
         elif  alive_sub == False:
            self.stone_factor.append(stone_now) 
            break
         else:
            pass
         sleep(0.1)  
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
def main_run():
   if len(sys.argv) == 2 :
      time_start=time()
      jiu_len=int(sys.argv[1])
      roof=make_I(jiu_len)
      st_this=stone(jiu_len,roof)
      #print st_this.get_stone()
      st_this.stone_prime_start()         
      result=1
      factor_list=st_this.get_stone_factor()
      for st in  factor_list:
         result=result*st
      print factor_list,result         
      time_end=time()
      st_this.f_log.write('time used is '+str((time_end-time_start)/60)+' minutes for '+str(jiu_len)+'\n')
      
   elif len(sys.argv) == 3:
      f_result=FileIO('stone.table','a')
      for arg in range(int(sys.argv[1]),int(sys.argv[2])):
         time_start=time()
         roof=make_I(arg)
         st_this=stone(arg,roof)
         st_this.stone_prime_start()
         result=1
         factor_list=st_this.get_stone_factor()
         for st in  factor_list:
            result=result*st
         str_result=str(arg)+':'+str(st_this.get_stone())+'='+str(factor_list)
         if result != st_this.get_stone(): 
            str_result=str_result+str(result)
         else:
            str_result=str_result+';'
         #if factor_list[-1] > st_this.roof:
         #   str_result=str_result+str(st_this.roof)
         f_result.write(str_result)
         st_this.f_log.write(str_result)
         print str_result
         time_end=time()
         st_this.f_log.write('time used is '+str((time_end-time_start)/60)+' minutes for '+str(arg)+'\n')
   #      del st_this
   else:
       print './stone_son.py num'
       print './stone_son.py min max'

if __name__ == "__main__":
   main_run()
