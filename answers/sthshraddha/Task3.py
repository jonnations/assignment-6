#!/usr/bin/env python

from math import factorial
import sys
sys.setrecursionlimit(3000)


def euler_calculation(n=0):
    if n>1000:
        return 0
    else:
        return (1/factorial(n)+euler_calculation(n+1))


def main():
    euler_value=euler_calculation()
    print (euler_value)


if __name__ == '__main__':
    main()
