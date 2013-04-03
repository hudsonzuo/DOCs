#!/usr/bin/python2.6
import sys
from math import sqrt
class divide_small:
   def __init__(self,num):
     ii=2
     result=[]
     roof=int(sqrt(num))+1
     while ii < roof:
       if num % ii == 0:
         result.append(ii)
       ii = ii+1  
     self.factors=list(result)  
     for item in result:
        big=num/item
        if big > item:
           self.factors.append(num/item)
     self.num=num      
   def get(self):   
      return self.factors 
   def get_full(self):   
      if self.num >1:
         self.factors.append(self.num)
      return self.factors
if __name__ == "__main__":
   if len(sys.argv) >1:
      print divide_small(int(sys.argv[1])).get()
   else:
      print "./divide_small num"
      print "get_full(): get factors with itself"
      print "get(): get factors without itself"
