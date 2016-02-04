#!/usr/bin/env python
# encoding: utf-8

"""
 My third task for Assignment 6 demonstrating the use of the recursive function to compute Euler's number. 

 Created by A.J. Turner on February 3, 2016
 Copyright 2016 A.J. Turner. All rights reserved.


"""
import sys
sys.setrecursionlimit(1100)
from math import factorial

def example3(x):
	"""
	Program uses recursion to compute Euler's number (2.71828).
	"""
	
	if x >= 1000:
		return (1/(factorial(x)))
	else:
		return (1/(factorial(x))) + example3(x+1)

def main():
	x = 0
	print (example3(0))
	
if __name__ == '__main__':
    main()