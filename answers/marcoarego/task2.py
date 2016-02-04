# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:25:48 2016

@author: Marco
"""

'''
Task 2

Write a program that uses a recursive function to compute the sum of the 
integers from 0 to 1000 (inclusive). Return the sum of these numbers to the
main loop and print the result. Write the program to include a main() 
function and the ifmain statement.
'''
import sys

def pcblaster(x=0, lis=[]):
    ''' Function that sums all values from 0 to 1000 '''
    if x < 1001:
        lis.append(x)
        # where recursion magic happens!!        
        pcblaster(x+1)
    else: 
        pass
    return sum(lis)


def main():
    result = pcblaster()
    print (result)

if __name__ == '__main__':
    # I had to increase the recursion limit in order to run this function in my pc    
    sys.setrecursionlimit(1500)
    main()
    # Decreasing the recursion limit back to normal
    sys.setrecursionlimit(1000)