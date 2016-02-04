# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 08:20:38 2016

@author: Marco
"""

import math
import argparse

def recursion_for_e(maximum = 1000, x=0, z=1, n=1):
    '''
    This function is calculating the number e, with a recursion in a 
    if/else statement.
    This is the same function as before, but now with a new argument (maximum)
    that you can use to set the maximum recursion that you want
    '''
    # while loop
    if n < maximum:
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
    """ArgumentParser parses arguments through the parse_args() method. 
    This will inspect the command line, convert each argument to the 
    appropriate type and then invoke the appropriate action (Argparse Documentation)"""
    parse = argparse.ArgumentParser()
    # Adding an argument to 'parse'
    parse.add_argument("maximum", help="please enter the maximum iteration number to generate the Euler number after the script name", type=int)
    args = parse.parse_args()
    result = recursion_for_e(args.maximum)
    
    print ('\n'+str(result)+"\n\nThis Euler number was generated with the iteration number of "+str(args.maximum))

if __name__ == '__main__':
    main()