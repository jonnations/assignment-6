#!/usr/bin/env python
# utf-8

"""
My first chained conditional program
Created by Pramod Pantha on 3 Feb, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


def x_chained(x):
    """
    This function tells whether x is >, equal to, or < x
    Reference:http://www.pythonlearn.com/html-009/book004.html
    """

    if x > 10:
        return "x is greater than 10"
    elif x == 10:
        return "x is equal to 10"
    else:
        return "x is less than 10"


def main():
    answer = x_chained(11)
    print(answer)

if __name__ == '__main__':
    main()
