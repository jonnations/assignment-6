#!/usr/bin/env python

"""
Task1:
Write your own program that demonstrates the use of chained conditionals within
a function to accomplish a (relatively simple) task. You choose what the task
is. Write the program to include a main() function and the ifmain statement.

Created by Shraddha Shrestha on February 2, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


def task1():
    number_of_correct_answers=10
    if number_of_correct_answers>=9:
        print("PASS, EXCELLENT!")
    elif 8>number_of_correct_answers>=5:
        print("PASS, OKAY!")
    else:
        print("FAIL,BOO!")


def main():
    task1()

if __name__ == '__main__':
    main()
