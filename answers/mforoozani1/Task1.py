#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task1
"""


def function_1(x):
    if (0 < x) and (x < 2):
        x = x + 3
        print(x)
    elif x % 2 == 0:
        x = x / 2
        print(x)
    else:
        print(x)


def main():
    function_1(1)

if __name__ == '__main__':
    main()
