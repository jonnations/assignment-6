#!/usr/bin/env python
# #encoding: utf-8

"""
Program made using recursive function to approximate the value of e. This Program
also allows user input by the argparse module. To make this program work there
is no prompt on the screen for the user. They would just go to their command
line and run the program usin python with a value after it. For example:
$python reigeltask5_6.py 1000
If the value is above the maximum the program won't work and they will get a
recursion error.

Created by Alicia Reigel. 4 February 2016.
Copyright Alicia Reigel. Louisiana State University. 4 February 2016.

"""
import argparse
import sys
sys.setrecursionlimit(1500)
from math import factorial

def using_parser():
    """the function parses the user input and sends it back to main"""
    parser = argparse.ArgumentParser(description='approxmiate e')
    parser.add_argument("user_max_limit",help='gives max for e calculation', type=int)
    args = parser.parse_args()
    return args.user_max_limit
    #above statement takes the user max limit and returns it to the main loop

def calculates_e_recursion_style(x, y):
    """calculates a value for e using recursion"""
    if x<=y:
        return (1/(factorial(x))) + calculates_e_recursion_style(x+1, y)
    else:
        return 0

def main():
    y=using_parser()
        #this takes the user input and makes it a variable
    x=0
    if y>1500:
        print ("limit too large. Choose value less than 1500.")
    else:
        e=calculates_e_recursion_style(x, y)
        print("You approximation of e is:", end="")
        print(e)

if __name__ == '__main__':
    main()
