#!/usr/bin/python
import sys
class stone:
   def __init__(self,len_jiu=6):
#      print 'stone come for:',len_jiu
      self.len_jiu=len_jiu
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
   def get_stone(self):	 
      return self.stone_this
   def stone_factor(self):
      len_jiu=self.len_jiu
      factors=[]
      if len_jiu%2 == 0:
         start=len_jiu+1
         step=len_jiu
      else:
         start=len_jiu*2+1
         step=len_jiu*2
      end=self.stone_this/(len_jiu+1)+1
      print start,end,step
      beTry=start
      while beTry < end:
         if self.stone_this%beTry == 0:
	    factors.append(beTry)
	    factors.append(self.stone_this/beTry)
	    end=factors[-1]
	    print factors
	 beTry=beTry+step   
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
      st_this.get_stone()
      st_this.stone_factor()
