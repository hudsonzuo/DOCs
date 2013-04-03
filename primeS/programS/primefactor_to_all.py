#!/usr/bin/python2.6
# -*- encoding:utf-8 -*
class all_factors:
   def __init__(self,li_factor,li_power): 
      self.li_all=[]
      #print 'li_factor,li_power',li_factor,li_power
      if len(li_factor) != len(li_power):
         print 'error: len(li_factor) != len(li_power)'
         return None
      elif len(li_factor)==0:
         print 'error:len(li_factor)==0:'
         return None
      fac_tmp=[]
      len_primefactor = len(li_factor)
      for pow0 in range(0,li_power[0]+1):
         if len_primefactor > 1:
            for pow1 in range(0,li_power[1]+1):
               if len_primefactor > 2:
                  for pow2 in range(0,li_power[2]+1):
                     if len_primefactor > 3:
                        for pow3 in range(0,li_power[3]+1):
                           if len_primefactor > 4:
                              for pow4 in range(0,li_power[4]+1):
                                 if len_primefactor > 5:
                                    for pow5 in range(0,li_power[5]+1):
                                       if len_primefactor > 6:
                                          for pow6 in range(0,li_power[6]+1):
                                             fac_tmp.append(pow(li_factor[0],pow0)*pow(li_factor[1],pow1)*pow(li_factor[2],pow2)*pow(li_factor[3],pow3)*pow(li_factor[4],pow4)*pow(li_factor[5],pow5)*pow(li_factor[6],pow6))
                                       else:
                                          fac_tmp.append(pow(li_factor[0],pow0)*pow(li_factor[1],pow1)*pow(li_factor[2],pow2)*pow(li_factor[3],pow3)*pow(li_factor[4],pow4)*pow(li_factor[5],pow5))
                                 else:
                                    fac_tmp.append(pow(li_factor[0],pow0)*pow(li_factor[1],pow1)*pow(li_factor[2],pow2)*pow(li_factor[3],pow3)*pow(li_factor[4],pow4))
                           else:
                              fac_tmp.append(pow(li_factor[0],pow0)*pow(li_factor[1],pow1)*pow(li_factor[2],pow2)*pow(li_factor[3],pow3))
                     else:
                       fac_tmp.append(pow(li_factor[0],pow0)*pow(li_factor[1],pow1)*pow(li_factor[2],pow2))
               else:
                 fac_tmp.append(pow(li_factor[0],pow0)*pow(li_factor[1],pow1))
         else:
           fac_tmp.append(pow(li_factor[0],pow0))
      fac_tmp.sort()
      #print fac_tmp
      self.li_all.append(fac_tmp[0])
      for item in fac_tmp:
         if item != self.li_all[-1]:
            self.li_all.append(item)
      #self.li_all=self.li_all[0:-1]      
   def result(self):   
      return self.li_all
