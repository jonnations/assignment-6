#!/usr/bin/env python
# encoding: utf-8

"""
My 2nd program for Assignment 6

Created by Michael Henson on 03 Feb 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import sys
sys.setrecursionlimit(1500)

def funner(n):
    if n <= 1001:
        return n
    else:
        return (n + funner(n+1))



def main():
    x = funner(0)
    print(x)

if __name__ == '__main__':
    main()
