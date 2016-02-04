#!/usr/bin/env python
# encoding: utf-8

"""
 My fourth task for Assignment 6 demonstrating the use of user input within a recursive function. 

 Created by A.J. Turner on February 3, 2016
 Copyright 2016 A.J. Turner. All rights reserved.


"""

import sys

from math import factorial

def example3(x):
	"""
	Program uses recursion to compute Euler's number (2.71828), but asks for user input to proceed.
	"""
	
	if x ==0:
		return (1/(factorial(x)))
	else:
		return (1/(factorial(x))) + example3(x-1)
		
num = int(input("Please enter a number greater than or equal to 1000: ")) #asks user to enter a number to proceed
sys.setrecursionlimit(num+100)

def main():
	x = num
	print (example3(num))
	
if __name__ == '__main__':
    main()