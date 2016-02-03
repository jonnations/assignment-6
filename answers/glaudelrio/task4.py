# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 08:27:50 2016

@author: Glaucia
"""
"""
Task 4

Modify the program you created in Task 3, above, to accept user input where the user input is the 
maximum value of the range over which you compute e (you initially limited this to some value less 
than 1000). You cannot use the sum() function. Return the sum of these numbers (the value of e) to 
the main loop and print the result. Write the program to include a main() function and the ifmain 
statement.

"""

import sys
sys.setrecursionlimit(1500)
def Calc_e_rec(maximum=1000,initial=1,total=1,n=1):
    """ calculates Euler number using recursion, takes one initial value, one total value and an initial n value
    also takes a maximum value so you don't go up to infinity"""
    maximum=int(maximum)    
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

def main():
    #setting the input so we don't go to infinity:
    toplimit=input("Set the maximum value so we don't go to inifinity:")
    eulernumber=Calc_e_rec(maximum=toplimit)
    print(eulernumber)

if __name__ == "__main__":
    main()
