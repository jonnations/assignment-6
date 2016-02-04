# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:04:53 2016

@author: Marco
"""



"""
Task 1

Write your own program that demonstrates the use of chained conditionals 
within a function to accomplish a (relatively simple) task. You choose what 
the task is. Write the program to include a main() function and the ifmain 
statement.
"""

def loops(x=0): 
    '''
    This function will return if the inputed argument is zero, positive or
    negative
    '''
    if x < 0:
        return ("is negative")
        
    elif x == 0:
        return ("is zero")
        
    else:
        return ("is positive")

def main(x):
    result = loops(x)
    
    print (str(x), result)

if __name__ == '__main__':    
    main(0)
    main(1)
    main(-1)
    
