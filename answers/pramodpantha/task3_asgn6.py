#!/usr/bin/env python
# utf-8

"""
My recursive function to compute Euler's value
Created by Pramod Pantha on 3 Feb, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""

import math
import sys
sys.setrecursionlimit(1200)


def recursive_e(n=0):

    if n > 1000:
        return 0
    else:
        return (1/math.factorial(n)) + recursive_e(n+1)


def main():
    e = recursive_e()
    print(e)


if __name__ ==  '__main__':
    main()
