#!/usr/bin/env python
# encoding: utf-8

"""
 My fifth task for Assignment 6 demonstrating the use of user input within a recursive function. 

 Created by A.J. Turner on February 3, 2016
 Copyright 2016 A.J. Turner. All rights reserved.


"""
import argparse
import sys
sys.setrecursionlimit(1100)
from math import factorial

def example3(x):
	"""
	Program uses recursion to compute Euler's number (2.71828), but asks for user input to proceed using the argparse module.
	"""
	
	if x ==0:
		return (1/(factorial(x)))
	else:
		return (1/(factorial(x))) + example3(x-1)
		
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("num", help="Manual calculation of Euler's number", type=int)
	args = parser.parse_args()
	
	result = example3(args.num)
	print ("The input was "+str(args.num)+" and e was calculated to be: "+str(result))
	
	
if __name__ == '__main__':
    main()