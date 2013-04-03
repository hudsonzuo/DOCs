#!/usr/bin/python
import sys
import fenJie
from math import sqrt
from multiprocessing import Process,Manager,cpu_count
class stone:
   def __init__(self,len_jiu=6):
#      print 'stone come for:',len_jiu
      I=self.make_I(len_jiu)
      factor_len_jiu=self.factor(len_jiu)
      if len(factor_len_jiu) == 0:
         self.stone_this=self.make_I(len_jiu)
      else:
         self.stone_this=self.make_I(len_jiu)
         while len(factor_len_jiu) > 0:
            self.stone_this=self.stone_this/stone(factor_len_jiu.pop()).get_stone()
      len_jiu_tmp=len_jiu
      while len_jiu_tmp%3==0:
         self.stone_this=self.stone_this/3
         len_jiu_tmp=len_jiu_tmp/3
      self.len_jiu=len_jiu
   def header_num(self,num,len_header=1):
      stop=1
      while len_header >0:
         stop=stop*10
	 len_header=len_header-1
      while num >stop:
         num=num/10
      return num
   def get_stone(self):	 
      return self.stone_this
   def get_factor(self):
      return self.factor
      
   def stone_prime(self):
      len_jiu=self.len_jiu
      manager=Manager()
      self.factor=[]
      factor_list=manager.list([])
      env=dict()
      p_sub=[]
      cpuCount=cpu_count()
      
      for helper in range(0, 5*cpuCount/4):
         if len_jiu%2 == 0:
            env['step']=len_jiu*5*cpuCount/4
            env['start']=len_jiu+1+len_jiu*(helper%5)+len_jiu*5*(helper/5)
         else:
            env['step']=len_jiu*10*cpuCount/4
            env['start']=len_jiu*2+1+len_jiu*2*(helper%5)+len_jiu*10*(helper/5)
	 if env['start']%10 == 5:
	    continue
         env['end']=int(sqrt(self.stone_this))+1
	 env['step_usual']=env['step']/5
	 print 'before sub:',self.stone_this,env
         p_sub.append(Process(target = self.stone_prime_sub, args = [self.stone_this,factor_list,env]))
	 p_sub[-1].start()
      for sub in p_sub: 	 
	 sub.join()
      if len(factor_list) > 0:
         factor_list.sort()
	 print factor_list
         self.factor.append(factor_list[0])
         for fac in factor_list[1:]:
            is_prime=True
            for prime in self.factor:
               if fac%prime == 0:
   	          is_prime=False
   	          break
   	    if is_prime==True:
               self.factor.append(fac)
      else:
         self.factor.append(self.stone_this)
         
   def stone_prime_sub(self,st,factors,env):
      print st,env
      has_prime_flag=False
      beTry=env['start']
      while beTry < env['end']:
         if st%beTry == 0:
	    has_prime_flag=True
   	    factors.append(beTry)
   	    son=st/beTry
            env['end']=int(sqrt(son))+1
            env['step']=env['step_usual']
	    print 'find a factor(maybe a prime):',beTry,st,son
   	    self.stone_prime_sub(son,factors,env)
   	    break
   	 beTry=beTry+env['step']
#	    print beTry,env['end']
      if has_prime_flag == False and st < self.stone_this:
         factors.append(st)
	 #print 'add :',st
      return factors	       
      
   def make_I(self,len_I):
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
        
        
   def factor(self,num):
      li_factor=[]
      ii=1
      for ii in range(2,num-1):
         if num % ii == 0:
            li_factor.append(ii)
      return li_factor
if __name__ == "__main__":
   if len(sys.argv) == 1:
      print 'I need a number'
      quit()
   if len(sys.argv) > 1:
      st_this=stone(int(sys.argv[1]))
      print st_this.get_stone()
      
      st_this.stone_prime()	 
      result=1
      factor_list=st_this.get_factor()
      for st in  factor_list:
         result=result*st
      print factor_list,result	 
      

