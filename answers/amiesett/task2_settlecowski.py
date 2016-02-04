#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 6 Task 3

Amie Settlecowski
4 Feb. 2016

This program sums values from 0 to 1,000 in a recursive function

Found help with issue of returning null instead of s value at:
http://stackoverflow.com/questions/11356168/return-in-recursive-function
"""
import sys


def sigma_recursive(x, n, s=0):
    # recursively sums integers [x,n] and stores in s
    if x <= n:
        s = s + x
        x = x + 1
        return sigma_recursive(x, n, s)
    else:
        return s


def main():
    # reset recursion limit
    sys.setrecursionlimit(1100)

    # assign returned value to sum_total
    sum_total = sigma_recursive(0, 1000)
    print(sum_total)

if __name__ == '__main__':
    main()
