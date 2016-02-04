#! /usr/bin/env python
# encoding: utf-8

'''
Task 1
Odd number summing program
By Grace Cagle 02 Feb 2016
'''


def odd_sums(x):
    total = 0
    for i in range(0, x):
        # for numbers in a range
        if i % 2 != 0:
            total += i
        # add to total if they are odd
    return total


def main():
    print(odd_sums(100))

if __name__ == '__main__':
    main()
