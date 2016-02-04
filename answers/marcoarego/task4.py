# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 08:10:01 2016

@author: Marco
"""

"""
Task 4

Modify the program you created in Task 3, above, to accept user input where
the user input is the maximum value of the range over which you compute e 
(you initially limited this to some value less than 1000). You cannot use the
sum() function. Return the sum of these numbers (the value of e) to the main 
loop and print the result. Write the program to include a main() function and 
the ifmain statement.
"""


import math

def recursion_for_e(maximum = 1000, x=0, z=1, n=1):
    '''
    This function is calculating the number e, with a recursion in a 
    if/else statement.
    This is the same function as before, but now with a new argument (maximum)
    that you can use to set the maximum recursion that you want.
    '''
    # while loop
    if n < int(maximum):
        # default values are x, z and n. These shall not be changed
        x = x+(1/z)
        # I used the math.factorial function to get factorial values
        z = math.factorial(n)
        n = n+1
        # recursion magic incorporating new values for x, z and n
        return recursion_for_e(maximum,x,z,n)
    else:
        return x
    

def main():
    # setting the 'input' variable that the user will insert later from the shell
    maximum = input('\n>>> Insert your maximum recursion number here: ')
    result = recursion_for_e(maximum)
    print (result)

if __name__ == '__main__':
    main()