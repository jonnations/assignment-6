#!/usr/bin/env python
# encoding: utf-8

"""
My 4th program for Assignment 6

Created by Michael Henson on 03 Feb 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import sys
import math
sys.setrecursionlimit(1500)

def funner(n, x):

    if n > x:
        return (1/math.factorial(n))
    else:
        return (1/math.factorial(n)) + funner(n+1, x)



def main():
    question = "What is the limit you want to run for calculating e?"
    x = int(input(question))
    z = funner(0, x)
    print(z)

if __name__ == '__main__':
    main()
