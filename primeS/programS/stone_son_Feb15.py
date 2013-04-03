#!/usr/bin/python2.6
import sys
import fenJie
from math import sqrt
from multiprocessing import Process,Manager,cpu_count
from io import FileIO
from time import sleep
class stone:
   def __init__(self,jiu_len=6):
#      print 'stone come for:',jiu_len
      I=self.make_I(jiu_len)
      factor_jiu_len=self.factor(jiu_len)
      if len(factor_jiu_len) == 0:
         self.stone_this=self.make_I(jiu_len)
      else:
         self.stone_this=self.make_I(jiu_len)
         while len(factor_jiu_len) > 0:
            self.stone_this=self.stone_this/stone(factor_jiu_len.pop()).get_stone()
      jiu_len_tmp=jiu_len
      while jiu_len_tmp%3==0:
         self.stone_this=self.stone_this/3
         jiu_len_tmp=jiu_len_tmp/3
      self.jiu_len=jiu_len
      self.stone_factor=[]
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
   def get_stone_factor(self):
      return self.stone_factor
      
#   def stone_prime(self):
#      jiu_len=self.jiu_len
#      manager=Manager()
#      self.stone_factor=[]
#      factor_list=manager.list([])
#      env=dict()
#      p_sub=[]
#      #cpuCount=cpu_count()
#      cpuCount=8
#      
#      for helper in range(0, 5*cpuCount/4):
#         if jiu_len%2 == 0:
#            env['step']=jiu_len*5*cpuCount/4
#            env['start']=jiu_len+1+jiu_len*(helper%5)+jiu_len*5*(helper/5)
#         else:
#            env['step']=jiu_len*10*cpuCount/4
#            env['start']=jiu_len*2+1+jiu_len*2*(helper%5)+jiu_len*10*(helper/5)
#	 if env['start']%10 == 5:
#	    continue
#         env['end']=int(sqrt(self.stone_this))+1
#         env['step_usual']=env['step']/5
#         print 'before sub:',self.stone_this,env
#         p_sub.append(Process(target = self.stone_prime_sub, args = [self.stone_this,factor_list,env]))
#	 p_sub[-1].start()
#      p_master=Process(target = self.stone_prime_master, args = [factor_list,p_sub])
#      p_master.start()
#      p_master.join()
#      for sub in p_sub: 	 
#	 sub.join()
   	 
#      if len(factor_list) > 0:
#         factor_list.sort()
#	 print factor_list
#         self.factor.append(factor_list[0])
#         for fac in factor_list[1:]:
#            is_prime=True
#            for prime in self.factor:
#               if fac%prime == 0:
#   	          is_prime=False
#   	          break
#   	    if is_prime==True:
#               self.factor.append(fac)
#      else:
#         self.factor.append(self.stone_this)
	    
   def stone_prime_sub(self,st,factors,env):
      #print st,env,factors
      has_prime_flag=False
      beTry=env['start']
      while beTry < env['end']:
         if st%beTry == 0:
	    has_prime_flag=True
   	    factors.append(beTry)
   	    #son=st/beTry
            #env['end']=int(sqrt(son))+1
            #env['step']=env['step_usual']
	    #print 'find a factor(maybe a prime):',beTry,st,son
	    print 'find a factor(maybe a prime):',beTry,st
   	    #self.stone_prime_sub(son,factors,env)
   	    #break
         elif beTry >self.make_I(10):
            return []
   	 beTry=beTry+env['step']
         #print beTry,env['end']
      if has_prime_flag == False and st < self.stone_this:
         factors.append(st)
      elif has_prime_flag == False and st==self.stone_this and env['step']==self.jiu_len:
         factors.append(st)
          
	 #print 'add :',st
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
      #for sub in p_sub: 	 
#	 sub.join()
      
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
            print 'before, stone_factor=',self.stone_factor
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
            print 'after ,stone_factor=',self.stone_factor
#            factors=[]
#            env['start']=jiu_len*(jiu_len%2+1)+1
#            env['step']=jiu_len*(jiu_len%2+1)
#            print 'before, stone_factor=',self.stone_factor
#            self.stone_factor=self.stone_factor+self.stone_prime_sub(factor_list[0],factors,env)
#            print 'after ,stone_factor=',self.stone_factor
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
#      turnOut=False
#      while True:
#         sleep(5)  
#	 prime_total=1
#	 if len(factor_list) >0:
#            factor_list.sort()
#   	    #print 'master has factors:',factor_list
#	    if len(self.stone_factor)==0:
#               self.stone_factor.append(factor_list[0])
#            for fac in factor_list[1:]:
#	       prime_total=1
#	       if fac <= self.stone_factor[-1]:
#	          continue
#               is_prime=True
#               for prime in self.stone_factor:
#                  if fac%prime == 0:
#      	             is_prime=False
#      	             break
#      	       if is_prime==True:
#                  self.stone_factor.append(fac)
#         for prime in self.stone_factor:
#	    #print prime_total,prime
#	    prime_total=prime_total*prime
#	 if prime_total >= self.stone_this:
#	    for sub in p_sub:
#	       if sub.is_alive():
#	          sub.terminate()
#            print 'master work finished(site1):',prime_total,self.stone_factor,self.stone_this
#	    break
#         alive_sub=False
#	 for sub in p_sub:
#	    if sub.is_alive():
#	       alive_sub=True
#	       break
#	 if alive_sub == False:
#	    if len(self.stone_factor) == 0:
#	       self.stone_factor.append(self.stone_this)
#            print 'master work finished(site2):',prime_total,self.stone_factor,self.stone_this
#	    break
         #print 'master working:',prime_total,self.stone_factor
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
   if len(sys.argv) == 2:
      st_this=stone(int(sys.argv[1]))
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
         st_this=stone(arg)
         st_this.stone_prime_start()
         result=1
         factor_list=st_this.get_stone_factor()
         for st in  factor_list:
            result=result*st
         print factor_list,result
         str_result=str(arg)+';'+str(factor_list)+';'+str(result)+';'
         if result != st_this.get_stone(): 
            str_result=str_result+str(st_this.get_stone())+'\n'
         else:
            str_result=str_result+'\n'
         f_result.write(str_result)
         #sleep(10) 
