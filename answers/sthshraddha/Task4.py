#!/usr/bin/env python

"""
Task4:
Modify the program you created in Task 3, above, to accept user input where the
user input is the maximum value of the range over which you compute e (you
initially limited this to some value less than 1000). You cannot use the sum()
function. Return the sum of these numbers (the value of e) to the main loop and
print the result. Write the program to include a main() function and the ifmain
statement.

Created by Shraddha Shrestha on February 4, 2016 after hundreds of attemps!
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""

from math import factorial
import sys
sys.setrecursionlimit(3000)


def euler_calculation(l,u):
    ##l=lower_limit, u=upper_limit
    if l > u:
        return 0
    else:
        return (1/factorial(l)) + euler_calculation(l+1,u)


def main():
    value = input("What upper_limit value would you like to use?")
    value_int = int(value)
    euler_number = euler_calculation(0,value_int)
    print (euler_number)


if __name__ == '__main__':
    main()
