#!/usr/bin/python2.6
import sys
import fenJie
from math import sqrt
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
	    
   def stone_prime_sub(self,st,factors,env):
      has_prime_flag=False
      beTry=env['start']
      while beTry < env['end']:
         if st%beTry == 0:
	    has_prime_flag=True
   	    factors.append(beTry)
	    print 'find a factor(maybe a prime):',beTry,st
         elif beTry >self.roof:
            return []
   	 beTry=beTry+env['step']
      if has_prime_flag == False and st < self.stone_this:
         factors.append(st)
      elif has_prime_flag == False and st==self.stone_this and env['step']==self.jiu_len:
         factors.append(st)
      return factors	       
   def stone_prime_start(self):
       self.stone_prime_master(self.stone_this)
   def stone_prime_master(self,stone_now):
      jiu_len=self.jiu_len
      manager=Manager()
      factor_list=manager.list([])
      env=dict()
      p_sub=[]
      cpuCount=cpu_count()
      #cpuCount=8
      for helper in range(0, 5*cpuCount/4):
         if jiu_len%2 == 0:
            env['step']=jiu_len*5*cpuCount/4
            env['start']=jiu_len+1+jiu_len*(helper%5)+jiu_len*5*(helper/5)
         else:
            env['step']=jiu_len*10*cpuCount/4
            env['start']=jiu_len*2+1+jiu_len*2*(helper%5)+jiu_len*10*(helper/5)
	 if env['start']%10 == 5:
	    continue
         env['end']=int(sqrt(stone_now))+1
         env['step_usual']=env['step']/(5*cpuCount/4)
         #print 'before sub:',self.stone_this,env
         p_sub.append(Process(target = self.stone_prime_sub, args = [stone_now,factor_list,env]))
	 p_sub[-1].start()
      
      turnOut=False
      while True:
         sleep(5)  
         #print factor_list,stone_now
         alive_sub=False
	 for sub in p_sub:
           if sub.is_alive():
	       alive_sub=True
	       break
	 prime_total=1
         if len(factor_list) >0:
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
            stone_now=self.stone_this
            for fa in self.stone_factor: 
               stone_now=stone_now/fa
            if stone_now >1 :
               self.stone_prime_master(stone_now)
               break
            else:
               return factor_list_new
         
         elif  alive_sub == False:
            self.stone_factor.append(stone_now) 
            break
         else:
            pass
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
if __name__ == "__main__":
   roof=make_I(23)
   if len(sys.argv) == 1:
      print 'I need a number'
      quit()
   if len(sys.argv) == 2:
      st_this=stone(int(sys.argv[1]),roof)
      print st_this.get_stone()
      
      st_this.stone_prime_start()	 
      result=1
      factor_list=st_this.get_stone_factor()
      for st in  factor_list:
         result=result*st
      print factor_list,result	 
      
   elif len(sys.argv) == 3:
      f_result=FileIO('stone.table','a')
      for arg in range(int(sys.argv[1]),int(sys.argv[2])):
         time_start=time()
         st_this=stone(arg,roof)
         st_this.stone_prime_start()
         result=1
         factor_list=st_this.get_stone_factor()
         for st in  factor_list:
            result=result*st
         str_result=str(arg)+';'+str(factor_list)+';'+str(result)+';'
         if result != st_this.get_stone(): 
            str_result=str_result+str(st_this.get_stone())+';'
         else:
            str_result=str_result+';'
         if factor_list[-1] > st_this.roof:
            str_result=str_result+str(st_this.roof)
         f_result.write(str_result)
         print str_result
         time_end=time()
         print 'time used is ',int((time_end-time_start)/60),' minutes'
