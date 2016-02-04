#!/usr/bin/env python
# utf-8

"""
Created by Pramod Pantha on 3 Feb, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""

import math
import argparse
import sys
sys.setrecursionlimit(1100)


def recursive_e(n, limit):

    if n == 0:
        return (1/math.factorial(n)) + recursive_e(n+1, limit)
    elif n <= limit:
        return (1/math.factorial(n)) + recursive_e(n+1, limit)
    else:
        return 0


def parser():
    """
    Creating arguments to which I can pass integer values. Pass args to
    recursive_e.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("ival", help="The changing number that cycles from 0" +
                        "to factoriallimit and must start at 0", type=int)
    parser.add_argument("flim", help="The factorial used to approximate e",
                        type=int)
    args = parser.parse_args()
    return recursive_e(args.ival, args.flim)


def main():
    e = parser()
    print(e)

if __name__ ==  '__main__':
    main()
