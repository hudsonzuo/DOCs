#!/usr/bin/python
import sys
import fenJie
from math import sqrt
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
      env=dict()
      if len_jiu%2 == 0:
         env['start']=len_jiu+1
         env['step']=len_jiu
      else:
         env['start']=len_jiu*2+1
         env['step']=len_jiu*2
      #env['end']=self.almost_sqrt(self.stone_this)
      env['end']=int(sqrt(self.stone_this))+1
#      if fenJie.factorS(len_jiu).get_factorList()==[]:
#         env['end']=self.make_I((len_jiu+1)/2)
#      else:	 
#         env['end']=self.stone_this/env['start']+1
      self.factor=[]
      self.stone_prime(self.stone_this,self.factor,env)	 
   def header_num(self,num,len_header=1):
      stop=1
      while len_header >0:
         stop=stop*10
	 len_header=len_header-1
      while num >stop:
         num=num/10
      return num
   def almost_sqrt(self,num):
      len_num=len(str(num))
      header=self.header_num(num)
      tmp=self.make_I(len_num)*header
      if tmp > num:
         master=header
      else:
         master=header+1
      if len_num%2==0:
         sqrt=self.make_I(len_num/2)*master
      else:   
         sqrt=self.make_I((len_num+1)/2)*master

      	 
      if sqrt*sqrt < num:
         
         print sqrt*sqrt,'less than',num
    #  print 'Notice:',num,len_num,header,tmp,master,sqrt
    #  print 'sqrt=',sqrt,'for ',num  	 
      return sqrt	 
   def get_stone(self):	 
      return self.stone_this
   def get_factor(self):
      return self.factor
   def stone_prime(self,st,factors,env):
      has_prime_flag=False
      print env
      for helper in range(0,5):
	 bigStep=env['step']*5
	 bigStart=env['start']+env['step']*helper
	 if bigStart%10 == 5:
	    continue
         beTry=bigStart
         while beTry < env['end']:
            if st%beTry == 0:
	       has_prime_flag=True
   	       factors.append(beTry)
	       print 'find a prime:',beTry,st
   	       son=st/beTry
   	       #env['end']=self.almost_sqrt(son)
               env['end']=int(sqrt(son))+1
   	       self.stone_prime(son,factors,env)
   	       break
   	    beTry=beTry+bigStep
#	    print beTry,env['end']
	 if has_prime_flag == True:
	    break
      if has_prime_flag == False and st < self.stone_this:
         factors.append(st)
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
      result=1
      factor_list=st_this.get_factor()
      for st in  factor_list:
         result=result*st
      print factor_list,result	 
      

