#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 6 demonstrating the use of chain conditionals. 

 Created by A.J. Turner on February 3, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

"""
 
def mychain(n): 
 
	"""
	This program takes a number (n) and runs it through chained conditional statements to see if it is equal to, greater than, or less than 50. A message is then printed based on how the number compares to 50
	"""
	#print (n)
	if n == 50:
		print ("Medium") #statement to print 'Medium' if n equals 50
	elif n > 50: #statement to print 'High' if n > 50
		print ("High")
	else: #statement to print 'Low' if n < 50
		print ("Low")

def main():
	n = 100
	mychain(n)
		
if __name__ == '__main__':
    main()