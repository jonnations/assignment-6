# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 20:56:36 2016

@author: Glaucia
"""
"""
In task-4 of Assignment-5, I asked you to write a function that computed Euler's number, return that 
value to the main loop of the program, and print that out.

This time, I want you to compute Euler's number using recursion - that is, use a function that calls 
itself to compute Euler's number, then return that value to the main loop and print the value you have 
returned to the screen. You cannot use the sum() function. Return the sum of these numbers (the value of e
) to the main loop and print the result. Write the program to include a main() function and the ifmain 
statement.
"""
import sys
sys.setrecursionlimit(1500)
def Calc_e_rec(initial=1,total=1,n=1,maximum=1000):
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
        return Calc_e_rec(initial,total,n=multiplication)
    else:
        #returns the total value, in other words the euler number
        return total

def main():
    eulernumber=Calc_e_rec()
    print(eulernumber)

if __name__ == "__main__":
    main()



