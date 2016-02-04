#!/usr/bin/env python
# encoding: utf-8
"""
functions for Conditionals.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import argparse
import sys
import math


def value_of_e(n):
    if n == 1:
        return 1
    else:
        return (1 / math.factorial(n) + value_of_e(n-1))


def main():
        parse = argparse.ArgumentParser()
        parse.add_argument("upper_limit", help="put upper limit" +
                           " integer along with file name.", type=int)
        args = parse.parse_args()
        result = value_of_e(args.upper_limit)

        print(str(result))

if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    main()
