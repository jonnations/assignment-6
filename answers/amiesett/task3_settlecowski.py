#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 6 Task 3

Amie Settlecowski
4 Feb. 2016

This program estimates Euler's number using a recursive function
"""
import sys
import math


def eulers_recursive(x, n, s=0):
    # recursively sums (1/n!) integers [x,n] and stores in s
    if x <= n:
        s = s + (1/math.factorial(x))
        x = x + 1
        return eulers_recursive(x, n, s)
    else:
        return s


def main():
    # reset recursion limit
    sys.setrecursionlimit(1100)

    # assign returned e estimate to e
    e = eulers_recursive(0, 1000)
    print("e is approxximately ", e)

if __name__ == '__main__':
    main()
