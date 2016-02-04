#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 6 Task 2
Jon Nations 2 Feb 2016
"""


import sys
sys.setrecursionlimit(1500)


def bigsum(n):
    if n == 1:
        return 1
    else:
        return (n + bigsum(n - 1))


def main():
    print(bigsum(1000))


if __name__ == '__main__':
    main()
