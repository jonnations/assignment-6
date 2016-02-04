#! /usr/bin/env python
# encoding: utf-8

'''
Task 2
Sum integers up to a number x
By Grace Cagle 02 Feb 2016
'''
import sys
sys.setrecursionlimit(1100)


def sum_ints(x):
    if x == 0:
        return x
        # stop at 0
    else:
        return x + sum_ints(x-1)


def main():
    print(sum_ints(1000))

if __name__ == '__main__':
    main()
