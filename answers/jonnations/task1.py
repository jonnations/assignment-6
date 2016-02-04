#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 6 Task 1
Jon Nations 2 Feb 2016
"""

def perfect(x):
    if x < 68:
        print('too cool')
    elif x == 68:
        print('perfect')
    else:
        print('too hot')

def main():
    perfect(70)

if __name__ == '__main__':
    main()
