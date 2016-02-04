#! /usr/bin/env python
# encoding: utf-8

'''
Task 3
Approximate Euler's numer to 'n'
By Grace Cagle 02 Feb 2016
'''

import math
import sys
sys.setrecursionlimit(1100)


def euler(n):
    x = 1
    for i in range(0, n):
        sum_e = (math.factorial(i))
    if n == 0:
        return x
    else:
        return x / sum_e * euler(n-1)


def main():
    print(euler(100))

if __name__ == '__main__':
    main()
