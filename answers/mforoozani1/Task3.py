#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task3
"""

import math
import sys


def task3(n=0):

    if n > 1000:
        return 0
    else:
        return (1/math.factorial(n)) + task3(n+1)


def main():
    var1 = task3()
    print(var1)

if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    main()
