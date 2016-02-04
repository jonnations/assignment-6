#!/usr/bin/env python
# #encoding: utf-8

"""
Program made using recursive function to sum the values from 0-1000. This Program
could also take any values between 0-100 and complete the same thing.

Created by Alicia Reigel. 3 February 2016.
Copyright Alicia Reigel. Louisiana State University. 3 February 2016.

"""
import sys
sys.setrecursionlimit(1100)

def dumb_sum(x):
    """calculates the sum all integers between 0 and x if x<=1000"""
    if x>=0 and x<=1000:
        y=((x*(x+1))/2)
        x=x+1
        dumb_sum(x)
        return y

def main():
    y=dumb_sum(1000)
    print(y)

if __name__ == '__main__':
     main()
