# !/usr/bin/env python
# encoding: utf-8

"""
My recursive summing program
Created by Andre Moncrieff on 2 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""
import sys
sys.setrecursionlimit(1100)

def recursion_sum(x):
    """
    Sums each integer from x down through zero.
    This function is based on solution #2 on the following page:
    http://www.python-course.eu/python3_recursive_functions.php
    
    """
    if x == 0:
        return 0
    else:
        return x + recursion_sum(x-1)

def main():
    answer = recursion_sum(1000)
    print(answer)

if __name__ ==  '__main__':
    main()
    