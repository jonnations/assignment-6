#!/usr/bin/env python
# #encoding: utf-8

"""
Program made using recursive function calculate e.

Created by Alicia Reigel. 3 February 2016.
Copyright Alicia Reigel. Louisiana State University. 3 February 2016.

"""

import sys
sys.setrecursionlimit(1100)
from math import factorial

def calculates_e_recursion_style(x=0):
    """calculates a value for e using recursion"""
    if x<1000:
        return (1/(factorial(x))) + calculates_e_recursion_style(x+1)
    else:
        return 0

def main():
    e=calculates_e_recursion_style()
    print(e)

if __name__ == '__main__':
    main()
