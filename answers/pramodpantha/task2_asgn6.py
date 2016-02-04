#!/usr/bin/env python
# utf-8

"""
My recursive function to compute sum
Created by Pramod Pantha on 3 Feb, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""

import sys
sys.setrecursionlimit(1001)


def recursive_sum(x):
    if x == 0:
        return 0
    else:
        return x + recursive_sum(x-1)


def main():
    answer = recursive_sum(1000)
    print(answer)

if __name__ == '__main__':
    main()
