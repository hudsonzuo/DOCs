#!/usr/bin/python2.6
import fenJie_small
from primefactor_to_all import all_factors
from stone_son import *
from JIU_len import JIU_len
import time
import sys
from io import FileIO

class factorS:
   def make_commonOdd(self,num_orig):
      num=num_orig
      dict_factor={'factor':2,'power':0}
      if  num%2 == 0 :
         self.factor_list.append(2)
         self.factorpower_list.append(1)
         num=num/2
         while  num%2 == 0 :
            self.factorpower_list[-1]=self.factorpower_list[-1]+1
            num=num/2
      if  num%5 == 0 :
         self.factor_list.append(5)
         self.factorpower_list.append(1)
         num=num/5
         while  num%5 == 0 :
            self.factorpower_list[-1]=self.factorpower_list[-1]+1
            num=num/5
      return num   
   def __init__(self,num):
      self.f_log=FileIO('./log/fenJie.log','a')
      self.factor_list=[]
      self.factorpower_list=[]
      num_common=self.make_commonOdd(num)
      self.f_log.write('==========================================================================\n')
      self.f_log.write('start factorS,working on '+str(num)+':::::'+str(num_common)+'\n')
      if num_common < 1000 and num_common >1:
         self.factor_list.extend(fenJie_small.factorS_small(num_common).get_primtfactor())
         self.factorpower_list.extend(fenJie_small.factorS_small(num_common).get_factor_power())
      elif num_common >= 1000:	    
         jiu_len=JIU_len(num_common).result()
         if(jiu_len == num_common-1):
            self.factor_list.append(num_common)
            self.factorpower_list.append(1)
            return
         factor_jiu_len_list=factorS(jiu_len).get_all_factors()
         self.f_log.write('working on '+str(num_common)+' its JIU='+str(jiu_len)+':'+str(factor_jiu_len_list)+'\n')
         toBeTry_list=[]
         for factor in factor_jiu_len_list:
   	    st_this=stone(factor,num)
	    st_this.stone_prime_start()
	    stone_factor_list=st_this.get_stone_factor()
            self.f_log.write('working on '+str(num_common)+' stone_factor_list for '+str(factor)+':'+str(stone_factor_list)+'\n')
	    if len(stone_factor_list) ==0 :
               #if (st_this.get_stone() < num_common):
   	       toBeTry_list.append(st_this.get_stone())
	    else:   
               for totry in stone_factor_list:
               #   if(totry < num_common):
	          toBeTry_list.append(totry)
	 self.f_log.write('working on '+str(num_common)+' toBeTry'+str(toBeTry_list)+'num_common='+str(num_common)+'\n')
         for maybe in toBeTry_list:
            if num_common % maybe ==0:
               self.factor_list.append(maybe)
               self.factorpower_list.append(1)
               num_common=num_common/maybe
               while num_common % maybe ==0:
                  num_common=num_common/maybe
                  self.factorpower_list[-1]= self.factorpower_list[-1]+1
      #print time.ctime()
   def get_factor_power(self):
      return self.factorpower_list
   def get_factorS(self):
      return self.factor_list   
   def get_all_factors(self):
      return all_factors(self.factor_list,self.factorpower_list).result() 

   	       #odd_factor_list.append(num_odd/maybe)
      #len(odd_factor_list) is even
#      if len(odd_factor_list) == 0 and len(even_factor_list)==0:
#         self.factor_list=[]
#      elif len(odd_factor_list) == 0 and len(even_factor_list) != 0:
#         even_factor_list.sort()
#         for fa in even_factor_list:
#	    self.factor_list.append(fa)
#	    if fa != even_factor_list[-1] and num_odd>1:
#	       self.factor_list.append(fa*num_odd)
#	 if num_odd > 1:      
#	    self.factor_list.append(num_odd)      
#            odd_factor_list.append(num_odd)
#      elif len(odd_factor_list) != 0 and len(even_factor_list) == 0:
#         odd_factor_list.sort()
#         for fa in odd_factor_list:
#	    self.factor_list.append(fa)
#      elif len(odd_factor_list) != 0 and len(even_factor_list) != 0:
#         even_factor_list.sort()
#         odd_factor_list.append(num_odd)
#         odd_factor_list.sort()
#         for fa_even in even_factor_list:
#	    self.factor_list.append(fa_even)
#            for fa_odd in odd_factor_list:
#	        self.factor_list.append(fa_odd*fa_even)
#         for fa_odd in odd_factor_list:
#	    self.factor_list.append(fa_odd)
      #self.factor_list.sort()	    
#      if len(self.factor_list)>0 and self.factor_list[-1]==num:
#         self.factor_list.pop()
if __name__ == "__main__":
   fac_this=factorS(int(sys.argv[1]))
   print fac_this.get_all_factors()
   print fac_this.get_factorS(),'by power:',fac_this.get_factor_power()

