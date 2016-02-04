# !/usr/bin/env python
# encoding: utf-8

"""
My chained conditional program
Created by Andre Moncrieff on 2 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""


def x_evaluation(x):
    """
    This function tells the user whether x is >, equal to, or < 5
    """
    if x > 5:
        return "x is greater than five"
    elif x == 5:
        return "x is equal to five"
    else:
        return "x is less than five"

def main():
    answer = x_evaluation(5.2)
    print(answer)

if __name__ ==  '__main__':
    main()
    

         