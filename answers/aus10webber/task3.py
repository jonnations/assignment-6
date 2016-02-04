#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 6, Task 3
Austen T. Webber
2016_2_2
"""

from math import factorial
import sys

sys.setrecursionlimit(1500)

# Calculate e recursively
def computer_killer(x=0):
    if x < 1000:
        return (1/(factorial(x))) + computer_killer(x+1)
    else:
        return 0

def e_recursion():
    e = computer_killer()
    print(e)

if __name__ == '__main__':
    e_recursion()
