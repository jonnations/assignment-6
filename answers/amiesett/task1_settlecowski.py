#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 6 Task 1

Amie Settlecowski
4 Feb. 2016

This program determines whether the integer assigned to test is odd, even, or 0
"""


def odd_even(x):
    # takes integer x and returns whether odd, even, 0
    if x == 0:
        return '0'
    elif (x % 2) == 0:
        return 'even'
    elif (x % 2) == 1:
        return 'odd'


def main():
    # this variable must be assigned an integer value
    test = 556
    print(odd_even(test))

if __name__ == '__main__':
    main()
