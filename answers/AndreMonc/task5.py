# !/usr/bin/env python
# encoding: utf-8

"""
My e-finding argparse program
Created by Andre Moncrieff on 3 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.

For this function to work, you need to type the following into terminal after 
the prompt:

python task5.py 0 whateverrangeyouwant

Thus, the following would work:
python task5.py 0 750


"""

import math
import argparse
import sys
sys.setrecursionlimit(1100)

def e_recur(i, limit):
    """
    This function approximates the value of e using recursion
    """   
    if i == 0:
        return (1/math.factorial(i)) + e_recur(i+1, limit)
    elif i <= limit:
        return (1/math.factorial(i)) + e_recur(i+1, limit)
    else:
        return 0

def parser():   
    """
    Creating arguments to which I can pass integer values. Pass args to e_recur. 
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("ival", help="The changing number that cycles from 0" + 
                         "to factoriallimit and must start at 0", type=int)
    parser.add_argument("flim", help="The factorial used to approximate e", 
                        type=int)   
    args = parser.parse_args()
    return e_recur(args.ival, args.flim)
    
def main():
    e = parser()
    print(e)
    
if __name__ ==  '__main__':
    main()
    
