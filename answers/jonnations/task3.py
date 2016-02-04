#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 6 Task 3
Jon Nations 2 Feb 2016
"""

from math import factorial


def getting_e(n):
    if n >= 800:
        return 1+(1/factorial(n))
    else:
        return (1/factorial(n)) + getting_e(n+1)


def main():
    print(getting_e(1))

if __name__ == '__main__':
    main()
