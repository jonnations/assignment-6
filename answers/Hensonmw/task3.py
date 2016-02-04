#!/usr/bin/env python
# encoding: utf-8

"""
My 3rd program for Assignment 6

Created by Michael Henson on 03 Feb 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import sys
sys.setrecursionlimit(10000)
import math

def funner(n):
    if n > 1000:
        return (1/math.factorial(n))
    else:
        return (1/math.factorial(n)) + funner(n+1)

def main():
    x = funner(0)
    print(x)

if __name__ == '__main__':
    main()
