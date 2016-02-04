#!/usr/bin/env python
# encoding UTF-8

'''
biol7800 
ZacCarver
02042016

Task5-modify prog from task4 to accept input from the user using the argparse
module. group the use of argparse into its own fxn. return to main loop and
print result.
'''
import sys
import math
import argparse
sys.setrecursionlimit(5000)


def argp():
    parser = argparse.ArgumentParser(description='get approx for e')
    parser.add_argument("max", type=int)
    args = parser.args()
    return args.max


def a6t5(ge):
    if ge >= 1000:
        return 1+(1/math.factorial(ge))
    else:
        return (1/math.factorial(ge)) + a6t5(ge+1)


def main():
    argp()
    a6t5(1)

if __name__ == '__main__':
    main()
