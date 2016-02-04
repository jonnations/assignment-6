#!/usr/bin/env python

"""
Task5:
Modify the program you created in Task 4, above, to accept input from the user
using the argparse module. You'll need to looks at the argparse documentation
to learn how the module works. Group the use of argparse into its own function.
As before, you cannot use the sum() function. Return the sum of these numbers
(the value of e) to the main loop and print the result. Write the program to
include a main() function and the ifmain statement.

Created by Shraddha Shrestha on February 4, 2016 after watching YouTube video.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""

from math import factorial
import sys
import argparse
sys.setrecursionlimit(3000)


def euler_calculation(l,u):
    ## l is lower_limit, u is upper_limit
    if l > u:
        return 0
    else:
        return (1/factorial(l)) + euler_calculation(l+1,u)


def main():
    parser= argparse.ArgumentParser()
    parser.add_argument("UP", type=int, help="should be less than 1000")
    args = parser.parse_args()
    result=euler_calculation(0,args.UP)
    print (result)


if __name__ == '__main__':
    main()
