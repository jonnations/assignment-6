#!/usr/bin/env python
# #encoding: utf-8

"""
Program made using recursive function to sum the values from 0-1500 with the
maximum value set by the input from the user. It then prints the approximate of
e to the screen.

Created by Alicia Reigel. 3 February 2016.
Copyright Alicia Reigel. Louisiana State University. 3 February 2016.

"""
import sys
sys.setrecursionlimit(1500)
from math import factorial

def calculates_e_recursion_style(x, y):
    """calculates a value for e using recursion"""
    if x<=y:
        return (1/(factorial(x))) + calculates_e_recursion_style(x+1, y)
    else:
        return 0

def main():
    print("Choose a maximum value of x between 0 and 1500.")
    y = int(input())
    #user to input the maximum value for y and then turns in into an integer
    x=0
    e=calculates_e_recursion_style(x, y)
    print(e)

if __name__ == '__main__':
    main()
