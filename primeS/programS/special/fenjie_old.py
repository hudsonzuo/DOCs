#!/usr/bin/python
import sys
from math import sqrt
num=int(sys.argv[1])
print num
ii=2
#while ii < int(sqrt(num))+1:
while ii < num:
   if num % ii == 0:
      print ii
   ii = ii+1  

