#!/usr/bin/env python

"""
Task2:
Getting the sum of integers from 0 to 1000 (inclusive).
Credit url:
http://stackoverflow.com/questions/19966290/recursive-function-to-calculate
-sum
Contributed by: inspectorG4dget
Date accessed: 3rd Feb, 2016
Also, without setting the recursion limit, it will say:
RecursionError: maximum recursion depth exceeded, so we'll have to import
sys and then set recursion limit.
Credit url:
http://stackoverflow.com/questions/3323001/maximum-recursion-depth.
Contributed by: Scharron
Date accessed: 3rd Feb, 2016

Created by Shraddha Shrestha on February 3, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""
import sys
sys.setrecursionlimit(2000)


def sum_of_integers(n):
    if not n:
        return 0
    else:
        return n + sum_of_integers(n - 1)


def main():
    print (sum_of_integers(1000))


if __name__ == '__main__':
    main()
