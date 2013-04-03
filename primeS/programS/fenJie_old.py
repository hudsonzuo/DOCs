#!/usr/bin/python2.6
from stone_son import *
from JIU import *
import sys
import time
class factorS:
   def odd(self,num_orig,factor_list):
      factor_2=1
      num=num_orig
      while  num%2 == 0 :
         factor_2=factor_2*2
         factor_list.append(factor_2)
         num=num/2
      factor_5=1
      while  num%5 == 0 :
         factor_5=factor_5*5
         factor_2_tmp=factor_2
	 while factor_2_tmp>1:
	    factor_list.append(factor_5*factor_2_tmp)
	    factor_2_tmp=factor_2_tmp/2
         factor_list.append(factor_5)
         num=num/5
      if len(factor_list) >0 and factor_list[-1] == num_orig:
         factor_list.pop()
      return num   
   def __init__(self,num):
      self.factor_list=[]
      even_factor_list=[]
      odd_factor_list=[]
      num_odd=self.odd(num,even_factor_list)
      if num_odd < 100:
         ii=1
         for ii in range(3,num_odd-1):
            if num_odd % ii == 0:
               odd_factor_list.append(ii)
      else:	    
         jiu_len=JIU(num_odd).get_JIU_len()
         factor_jiu_len_list=factorS(jiu_len).get_factorList()
         stone_list=[]
         print num_odd,jiu_len,factor_jiu_len_list
         toBeTry_list=[]
         for factor in factor_jiu_len_list:
   	    st_this=stone(factor)
	    st_this.stone_prime()
	    factor_list=st_this.get_factor()
	    if len(factor_list) ==0 :
   	       toBeTry_list.append(st_this.get_stone())
	    else:   
	       for totry in st_this.get_factor():
	          toBeTry_list.append(totry)
	 print 'stone_list',stone_list   
         toBeTry_list.append(3)	 
	 print 'toBeTry',toBeTry_list
         for maybe in toBeTry_list:
            if num_odd % maybe ==0:
   	       odd_factor_list.append(maybe)
   	       odd_factor_list.append(num_odd/maybe)
      #len(odd_factor_list) is even
      if len(odd_factor_list) == 0 and len(even_factor_list)==0:
         self.factor_list=[]
      elif len(odd_factor_list) == 0 and len(even_factor_list) != 0:
         even_factor_list.sort()
         for fa in even_factor_list:
	    self.factor_list.append(fa)
	    if fa != even_factor_list[-1] and num_odd>1:
	       self.factor_list.append(fa*num_odd)
	 if num_odd > 1:      
	    self.factor_list.append(num_odd)      
            odd_factor_list.append(num_odd)
      elif len(odd_factor_list) != 0 and len(even_factor_list) == 0:
         odd_factor_list.sort()
         for fa in odd_factor_list:
	    self.factor_list.append(fa)
      elif len(odd_factor_list) != 0 and len(even_factor_list) != 0:
         even_factor_list.sort()
         odd_factor_list.append(num_odd)
         odd_factor_list.sort()
         for fa_even in even_factor_list:
	    self.factor_list.append(fa_even)
            for fa_odd in odd_factor_list:
	        self.factor_list.append(fa_odd*fa_even)
         for fa_odd in odd_factor_list:
	    self.factor_list.append(fa_odd)
      self.factor_list.sort()	    
      if len(self.factor_list)>0 and self.factor_list[-1]==num:
         self.factor_list.pop()
      print odd_factor_list
      print even_factor_list
      print num,'=',self.factor_list   
      print time.ctime()
   def get_factorList(self):
      return self.factor_list   
      
if __name__ == "__main__":
   result=factorS(int(sys.argv[1])).get_factorList()

