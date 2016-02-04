#!/usr/bin/env python
# utf-8

"""
Assignment 6
Task 2 Program: Recursive functions
Jessie Salter
2 February 2016
"""

import sys

sys.setrecursionlimit(1500)

INT_LIST = list()


def gauss(x):
    """sums the values 0 to 1000"""
    if 0 <= x <= 1000:
        INT_LIST.append(x)
        x += 1
        gauss(x)
    answer = sum(INT_LIST)
    return answer


def main():
    answer = gauss(0)
    print(answer)


if __name__ == '__main__':
    main()
