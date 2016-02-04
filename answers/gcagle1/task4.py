#! /usr/bin/env python
# encoding: utf-8

'''
Task 4
Approximate Euler's numer to 'n'
With a user-input range
By Grace Cagle 02 Feb 2016
'''

import math
import sys
sys.setrecursionlimit(1100)


def euler(nterms):
    x = 1
    for i in range(0, nterms):
        sum_e = (math.factorial(i))
    if nterms == 0:
        return x
    else:
        return x / sum_e * euler(nterms-1)


def main():
    nterms = int(input("How many terms? "))
    print(euler(nterms))

if __name__ == '__main__':
    main()
