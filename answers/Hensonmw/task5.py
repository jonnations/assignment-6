#!/usr/bin/env python
# encoding: utf-8

"""
My 5th program for Assignment 6

Created by Michael Henson on 03 Feb 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import sys
import math
import argparse
sys.setrecursionlimit(1500)

def funner(n, x):

    if n > x:
        return (1/math.factorial(n))
    else:
        return (1/math.factorial(n)) + funner(n+1, x)

def userinput():

'''
https://docs.python.org/3/howto/argparse.html
'''
    parser = argparse.ArgumentParser()
    parser.add_argument("x", help="upper limit for e", type=int)
    parser.add_argument("n", help="lower limit for e, preferably 0", type=int)
    args = parser.parse_args()
    return funner(args.x, args.n)


def main():
    z = userinput()
    print(z)

if __name__ == '__main__':
    main()
