#!/usr/bin/env python
# utf-8

"""
Assignment 6
Task 5 Program: Recursive function to calculate e with argparse user input
Jessie Salter
2 February 2016
"""

import sys

import argparse

from math import factorial

sys.setrecursionlimit(1500)


def user_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("range_max", help="The maximum number of the range over \
    which you wish to compute e", type=int)
    args = parser.parse_args()
    return args.range_max


def e_recursive(x=0):
    """This function calculates the value of e recursively"""
    arg = user_input()
    if x < arg:
        return (1/(factorial(x))) + e_recursive(x+1)
        # This returns e
    else:
        return 0
        # This must be 0 because it will be added to the return value above


def main():
    user_input()
    e = e_recursive()
    print(e)


if __name__ == '__main__':
    main()
