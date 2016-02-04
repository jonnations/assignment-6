#!/usr/bin/env python
# encoding: utf-8
"""
functions for Conditionals.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import sys


def oneToN(n):
    if n == 1:
        return 1
    else:
        return n + oneToN(n-1)


def main():
    x = oneToN(1000)
    print(x)

if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    main()
