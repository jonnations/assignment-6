#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task3
"""

import math
import sys


import argparse


def task3(n=0):

    if n > 1000:
        return 0
    else:
        return (1/math.factorial(n)) + task3(n+1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("max", type=int)
    args = parser.parse_args()
    var1 = task3()
    print(str(var1) + str(args.max))

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    main()
