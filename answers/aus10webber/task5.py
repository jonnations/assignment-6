#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 6, Task 4
Austen T. Webber
2016_2_2
"""
from math import factorial
import sys
import argparse

sys.setrecursionlimit(1500)

# Let the user pick inputs
def test():
    parser = argparse.ArgumentParser(description='calculate some recursive e stuff')
    parser.add_argument("too_big", help="Your input number is too big. You'll break your computer.", type=int)
    args = parser.parse_args()
    return args.too_big

# Calculate e recursively
def computer_killer(x=0):
    z = test()
    if x < z:
        return (1/(factorial(x))) + computer_killer(x+1)
    else:
        return 0

def e_recursion():
    test()
    e = computer_killer(0,y)
    print(e)

if __name__ == '__main__':
    e_recursion()
