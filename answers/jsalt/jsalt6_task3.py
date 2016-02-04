#!/usr/bin/env python
# utf-8

"""
Assignment 6
Task 3 Program: Recursive function to calculate e
Jessie Salter
2 February 2016
"""

import sys

from math import factorial

sys.setrecursionlimit(1500)


def e_recursive(x=0):
    """This function calculates the value of e recursively"""
    if x < 1000:
        return (1/(factorial(x))) + e_recursive(x+1)
        # This returns e
    else:
        return 0
        # This must be 0 because it will be added to the return value above


def main():
    e = e_recursive()
    print(e)


if __name__ == '__main__':
    main()
