# !/usr/bin/env python
# encoding: utf-8

"""
My recursive e-finding program with input
Created by Andre Moncrieff on 3 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import math
import sys
sys.setrecursionlimit(1100)


def e_recur(i=0, limit=0):
    """
    This function approximates the value of e using recursion
    """   
       
    if i == 0:
        question = "Up to what factorial would you like to calculate\nthe value of e? Input a number of 1000 or less and\npress Enter: "
        factorial_limit = int(input(question))
        return (1/math.factorial(i)) + e_recur(i+1, factorial_limit)
    elif i <= limit:
        return (1/math.factorial(i)) + e_recur(i+1, limit)
    else:
        return 0  
    
    
def main():  
    e = e_recur()
    print("Approximate value of e: ", e)

if __name__ ==  '__main__':
    main()
    
