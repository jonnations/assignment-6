#!/usr/bin/env python
# encoding UTF-8

'''
biol7800
ZacCarver
02042016

Task4-modify prog from task3 to accept user input wher the user input is the
value of the range over which e is computed, return to the main loop and print.
'''

import sys
import math
sys.setrecursionlimit(5000)


def a6t4(ge):
    if ge >= 1000:
        return 1+(1/math.factorial(ge))
    else:
        return (1/math.factorial(ge)) + a6t4(ge+1)


def main():
    ge = int(input("enter the limit for e-approximation: "))
    if ge == 1000:
        print(a6t4(1))
