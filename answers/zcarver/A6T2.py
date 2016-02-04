#!/usr/bin/env python
# encoding UTF-8

'''
biol7800
ZacCarver
02042016

Task2-use a recursive fxn to compute the sum of integers from 0-1000(inclusive)
Return the sum of these numbers to the main loop and print result. write to
include main() and ifmain statement.
'''
# http://www.composingprograms.com/pages/17-recursive-functions.html

import sys
sys.setrecursionlimit(5000)


def a6t2(f):
    if f == 0:
        return f
    else:
        return f + a6t2(f-1)


def main():
    sum1 = a6t2(1000)
    print(sum1)

if __name__ == '__main__':
    main()
