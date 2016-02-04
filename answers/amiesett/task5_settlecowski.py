#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 6 Task 5

Amie Settlecowski
4 Feb. 2016

This program estimates Euler's number, using a recursive function.
User input determines the upper limit of the range over which e is estimated.

***TO RUN***
python path/task5_settlecowski.py upper_limit
"""
import sys
import math
import argparse


def input_u():
    # parses user input and returns upper limit to main
    # source: https://youtu.be/rnatu3xxVQE
    parser = argparse.ArgumentParser()
    parser.add_argument("u_lim", help="Imports the upper limit  range"+'\n'+ "over which e is estimated", type = int)
    args = parser.parse_args()
    return args.u_lim


def eulers_recursive(x, n, s=0):
    # recursively sums (1/n!) integers [x,n] and stores in s
    if x <= n:
        s = s + (1/math.factorial(x))
        x = x + 1
        return eulers_recursive(x, n, s)
    else:
        return s


def main():
    # reset recursion limit
    sys.setrecursionlimit(1100)

    # define variaable for upper limit parsed from user input
    u_lim = input_u()

    # test that user input does not exceed recursion limit
    # source: Brant's assignment 5 task4.py
    if u_lim > 1095:
        print("Maximum of range exceeds limit of 1095")
        sys.exit()
    else:
        e = eulers_recursive(0, u_lim)
        print("e is approximately ", e)

if __name__ == '__main__':
    main()
