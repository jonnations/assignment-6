#!/usr/bin/env python
# encoding: utf-8
"""
functions for Conditionals.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import sys
import math


def value_of_e(n):
    if n == 1:
        return 1
    else:
        return (1 / math.factorial(n) + value_of_e(n-1))


def main():
    sth = int(input('what is the upper limit for calculation of e ?'))
    x = value_of_e(sth)
    print(x)

if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    main()
