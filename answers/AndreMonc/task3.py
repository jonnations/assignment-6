# !/usr/bin/env python
# encoding: utf-8

"""
My recursive e-finding program
Created by Andre Moncrieff on 3 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import math
import sys
sys.setrecursionlimit(1100)

def e_recur(i=0):
    """
    This function approximates the value of e using recursion
    """
    if i > 1000:
        return 0
    else:
        return (1/math.factorial(i)) + e_recur(i+1)
    
def main():
    e = e_recur()
    print(e)

if __name__ ==  '__main__':
    main()
    
