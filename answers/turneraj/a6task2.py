#!/usr/bin/env python
# encoding: utf-8

"""
 My second task for Assignment 6 demonstrating the use of the recursive function to compute the sum of integers. 

 Created by A.J. Turner on February 3, 2016
 Copyright 2016 A.J. Turner. All rights reserved.


"""
import sys
sys.setrecursionlimit(1100)

def example2(x):

	"""
	This program uses recursion to compute the sum of integers 0 to 1000
	"""
	if x >= 1000: #checks to see if value is >=1000
		return x #when 1000 is reached, 1000 is added to the end of the sum of x's
	else: #if value not 1000, line executed to give value of x and then puts x+1 in the function to run again
		return x + example2(x+1) 
		
def main():
	x = 0
	print (example2(x))
		
if __name__ == '__main__':
    main()