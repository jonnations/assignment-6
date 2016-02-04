#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 6 Task 4

Amie Settlecowski
4 Feb. 2016

This program estimates Euler's number, using a recursive function.
User input determines the upper limit of the range over which e is estimated.
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

    # assign returned value to sum_total
    u_lim = int(input("Enter the upper limit for estimating e: "))

    # test that user input does not exceed recursion limit
    # source: Brant's assignment 5 task4.py
    if u_lim > 1095:
        print("Maximum of range exceeds limit of 1095")
        sys.exit()
    else:
        e = eulers_recursive(0, u_lim)
        print("e is approximately ", e)

if __name__ == '__main__':
    main()
