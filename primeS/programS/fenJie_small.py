#!/usr/bin/python2.6
# -*- encoding:utf-8 -*
#仅用于分解小于100的整数
import sys
from primefactor_to_all import all_factors
class factorS_small:
   def __init__(self,num):
      table_prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89]
      self.primefactor=[]
      self.factor_power=[]
      for pri in table_prime:
         if num % pri ==0:
            self.primefactor.append(pri)   
            self.factor_power.append(1)
            num=num/pri
            while num % pri ==0:
               self.factor_power[-1]=self.factor_power[-1]+1
               num=num/pri
         if pri > num:
            #print num
            break

   def get_primtfactor(self):
      return self.primefactor
   def get_factor_power(self):
      return self.factor_power
   def get_all_factors(self):
      return all_factors(self.primefactor,self.factor_power)
if __name__ == "__main__":
   fa_this=factorS_small(int(sys.argv[1]))
   print 'factor:',fa_this.get_primtfactor()
   print 'power:',fa_this.get_factor_power()
   print 'all factors:',fa_this.get_all_factors()
            

         
