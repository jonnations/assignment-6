# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 08:51:02 2016

@author: Glaucia
"""
"""
Task 5

Modify the program you created in Task 4, above, to accept input from the user 
using the argparse module. You'll need to looks at the argparse documentation to 
learn how the module works. Group the use of argparse into its own function. 
As before, you cannot use the sum() function. Return the sum of these numbers (the value of e) 
to the main loop and print the result. Write the program to include a main() function 
and the ifmain statement.
"""

import sys
import argparse
sys.setrecursionlimit(1500)
def Calc_e_rec(maximum=1000,initial=1,total=1,n=1):
    """ calculates Euler number using recursion, takes one initial value, one total value and an initial n value
    also takes a maximum value so you don't go up to infinity"""  
    if initial <= maximum:
        #deals with factorials in the denominators of the equation 1/n!
        multiplication = n * (1/initial)
        #deals with the sum of fractions in the equation
        total = total + multiplication
        #changes the denominator to make the factorial multiplications keep going
        initial = initial+1
        #calls itself with new initial, total and n values so we can sum the total value until we reach 1000 as a denominator
        return Calc_e_rec(maximum,initial,total,n=multiplication)
    else:
        #returns the total value, in other words the euler number
        return total


def valid_toplimit():
    #creating a Argument Parser object and storing it in the parse variable
    parse = argparse.ArgumentParser()
    #this is going to tell the user to add the maximum argument in the comand prompt
    parse.add_argument("maximum", help="a maximum argument is required, type the number after python task5.py",type=int)
    #getting the string provided by the user and transforming in an object for my function   
    args = parse.parse_args()
    #this is going to run my function to calculate euler number, as soon as the user provide the maximum value    
    result=Calc_e_rec(args.maximum)
    print(result)
    
def main():
    valid_toplimit()

if __name__ == "__main__":
    main()