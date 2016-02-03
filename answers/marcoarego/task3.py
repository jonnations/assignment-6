# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 20:08:04 2016

@author: Marco
"""

'''
Task 3

In task-4 of Assignment-5, I asked you to write a function that computed 
Euler's number, return that value to the main loop of the program, and print 
that out.

This time, I want you to compute Euler's number using recursion - that is, 
use a function that calls itself to compute Euler's number, then return that 
value to the main loop and print the value you have returned to the screen. 
You cannot use the sum() function. Return the sum of these numbers (the value
of e) to the main loop and print the result. Write the program to include a 
main() function and the ifmain statement.
'''

import math
import sys

def recursion_for_e(x=0, z=1, n=1):
    '''
    This function is calculating the number e, with a recursion in a 
    if/else statement.
    '''
    # while loop
    if n < 1000:
        # default values are x, z and n. These shall not be changed
        x = x+(1/z)
        # I used the math.factorial function to get factorial values
        z = math.factorial(n)
        n = n+1
        # recursion magic incorporating new values for x, z and n
        return recursion_for_e(x,z,n)
    else:
        return x
    

def main():
    result = recursion_for_e()
    print (result)

if __name__ == '__main__':
     # I had to increase the recursion limit in order to run this function in my pc    
    sys.setrecursionlimit(1500)
    main()
    # Decreasing the recursion limit back to normal
    sys.setrecursionlimit(1000)
    
        
    