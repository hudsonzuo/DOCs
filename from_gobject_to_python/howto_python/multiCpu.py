# -*- coding:utf-8 -*-

import os
from multiprocessing import *

 

def test():
    while True:
        65535+65535

 

if __name__ == "__main__":
    for n in range(2):
        print "Proc(%d) Start..."%n
        p = Process(target = test, args = [])
        p.start()
