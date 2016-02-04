# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:30:34 2016

@author: Glaucia
"""
"""
Task 2

Write a program that uses a recursive function to compute the sum of the integers 
from 0 to 1000 (inclusive). Return the sum of these numbers to the main loop and print the result. 
Write the program to include a main() function and the ifmain statement.
"""

import sys
sys.setrecursionlimit(1500)


def sumnumbersinrange(currentsum=0,initial=1,final=1001):
    """sums all the numbers in a range that you can define with an initial and a final argument. Furthermore, you can also set
    a value that you want to add to your result (currentsum), the default for this value is 0"""
    #if the initial value is in the expected range it is going to keep adding values and reseting the initial value by recursion    
    if initial in list(range(final)):
        #resets the currentsum value, so stores the sum that you are aiming to have.
        currentsum = currentsum + initial
        #resets the initial value, so you always add the current sum to the next value in a range (in this case from 1 to 1001)
        initial= initial+1
        #calls the function again, now with the new values of currentsum and initial
        return sumnumbersinrange(currentsum,initial)
    else:
        #if the initial number is no longer in the expected range, returns the value stored in the currentsum after all recursions
        return currentsum
        
    

def main():
    result = sumnumbersinrange(currentsum=0,initial=1,final=1001)
    print(result)
    
    
if __name__ == "__main__":
    main()
    

  
    