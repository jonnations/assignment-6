#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 6 Task 4
Jon Nations 2 Feb 2016

"""

from math import factorial


def getting_e(n):
    if n >= 800:
        return 1+(1/factorial(n))
    else:
        return (1/factorial(n)) + getting_e(n+1)


def main():
    n = int(input("enter 800 as the value of n:  "))
    if n == 800:
        print(getting_e(1))

if __name__ == '__main__':
    main()
