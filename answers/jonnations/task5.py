#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 6 Task 5
Jon Nations 2 Feb 2016

"""

import argparse
from math import factorial


def getting_e(n):
    if n >= 800:
        return 1+(1/factorial(n))
    else:
        return (1/factorial(n)) + getting_e(n+1)


def argparsing():
    #this runs argparse. to run in pyton you must add the number 800
    #after the file name LIKE THIS ->  $ python task5.py 800
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int)
    args = parser.parse_args()

    result = getting_e(1)
    print("The estimate of e for n = " + str(args.num) + " is "+str(result))


def main():
    getting_e(1)
    argparsing()

if __name__ == '__main__':
    main()
