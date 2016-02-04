#!/usr/bin/env python
# encoding: utf-8

"""
My 1st program for Assignment 6

Created by Michael Henson on 03 Feb 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""

def fun(arg1):
    if arg1 > 8:
        return "Go State"
    else:
        return "Go Green"
def main():
    x = fun(9)
    print(x)

if __name__ == '__main__':
    main()
