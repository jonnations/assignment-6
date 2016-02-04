#!/usr/bin/env python
# encoding UTF-8

'''
biol7800
ZacCarver
02042016

Task3-compute Euler's number by recursion and return the value to the main loop
use the ifmain statement and main().
'''

import sys
import math
sys.setrecursionlimit(5000)


def a6t3(ge):
    if ge >= 1000:
        return 1+(1/math.factorial(ge))
    else:
        return (1/math.factorial(ge)) + a6t3(ge+1)


def main():
    print(a6t3(1))

if __name__ == '__main__':
    main()
