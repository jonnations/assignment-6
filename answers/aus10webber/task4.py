#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 6, Task 4
Austen T. Webber
2016_2_2
"""

from math import factorial
import sys

sys.setrecursionlimit(1500)

# Calculate e recursively
def computer_killer(x,y):
    if x < y:
        return (1/(factorial(x))) + computer_killer(x+1)
    else:
        return 0

def e_recursion():
    y=int(input("how many times do you want this to run?: "))
    e = computer_killer(0,y)
    print(e)

if __name__ == '__main__':
    e_recursion()
