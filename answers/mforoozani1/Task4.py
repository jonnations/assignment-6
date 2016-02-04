#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task3
"""

import math
import sys


def task3(max=1000, n=0):

    if n > int(max):
        return 0
    else:
        return (1/math.factorial(n)) + task3(max, n+1)


def main():
    max = input(' what is your max value?')
    var1 = task3(max)
    print(var1)

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    main()
