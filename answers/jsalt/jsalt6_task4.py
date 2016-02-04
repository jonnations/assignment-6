#!/usr/bin/env python
# utf-8

"""
Assignment 6
Task 4 Program: Recursive function to calculate e with user input
Jessie Salter
2 February 2016
"""

import sys

from math import factorial

sys.setrecursionlimit(1500)


def e_recursive(x, y):
    """This function calculates the value of e recursively"""
    if x < y:
        return (1/(factorial(x))) + e_recursive(x+1, y)
        # This returns e
    else:
        return 0
        # This must be 0 because it will be added to the return value above


def main():
    print("Enter the maximum value of the range over which you wish to sum e:")
    y = int(input())
    e = e_recursive(0, y)
    print(e)


if __name__ == '__main__':
    main()
