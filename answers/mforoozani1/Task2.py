#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2
"""
import sys


def sum_function(n):
    if n == 0:
        return 0
    return n + sum_function(n - 1)


def main():
    var1 = sum_function(1000)
    print(var1)

if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    main()
