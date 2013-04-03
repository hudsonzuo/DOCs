#!/usr/bin/python
from math import pow
def remainder(num,multi,prime):
   result=1
   print multi,
   while multi >0:
      result=result*num%prime
      multi=multi-1
   print result
   return result   
prime=241
#7, 70, 218, 11, 110, 136, 155, 104
root_num=7
result=[]
for multi in range(1,prime):
    result.append(remainder(root_num,multi,prime))
 #  remaind=pow(root_num,multi)%prime
 #  print multi,remaind
 #  result.append(remaind)
result.sort()
print root_num,result

oneYu_7=[7, 70, 218, 11, 110, 136, 155, 104, 76, 37, 129, 85, 127, 65, 168, 234, 171, 23, 230, 131, 105, 86, 137, 165, 204, 112, 156, 114, 176, 73]
result=[]
for yu in oneYu_7:
   tmp=yu*yu*yu*yu%prime
   result.append(tmp*tmp%prime)
result.sort()
#print result   

