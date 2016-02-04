#!/usr/bin/env python

"""
Task3:
This time, I want you to compute Euler's number using recursion - that is, use
a function that calls itself to compute Euler's number, then return that value
to the main loop and print the value you have returned to the screen. You
cannot use the sum() function. Return the sum of these numbers (the value of e)
to the main loop and print the result. Write the program to include a main()
function and the ifmain statement.

Created by Shraddha Shrestha on February 3, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""

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
