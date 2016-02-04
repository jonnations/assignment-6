#!/usr/bin/env python
# utf-8

"""
Created by Pramod Pantha on 3 Feb, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""
import math
import sys
sys.setrecursionlimit(1100)


def recursive_e(n=0, limit=0):

    if n == 0:
        question = "Up to what factorial would you like to calculate\nthe value of e? Input a number of 1000 or less and\npress Enter: "
        factorial_limit = int(input(question))
        return (1/math.factorial(n)) + recursive_e(n+1, factorial_limit)
    elif n <= limit:
        return (1/math.factorial(n)) + recursive_e(n+1, limit)
    else:
        return 0


def main():
    e = recursive_e()
    print("Approximate value of e: ", e)

if __name__ ==  '__main__':
    main()
