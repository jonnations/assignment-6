#!/usr/bin/env python
# encoding UTF-8

'''
biol7800
ZacCarver
02042016

Task1-demonstrate the use of chained conditionals within a fxn to accomplish a
relatively simple task. include main() and ifmain.
'''

import sys
sys.setrecursionlimit(5000)


def a6t1(b):
    if b != 1776:
        b = b * 1
        print("nobody")
    else:
        print("Volta")


def main():
    a6t1(1771)

if __name__ == '__main__':
    main()
