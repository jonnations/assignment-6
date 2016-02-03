# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:12:39 2016

@author: Glaucia
"""
"""
Task 1

Write your own program that demonstrates the use of chained conditionals within a 
function to accomplish a (relatively simple) task. You choose what the task is. 
Write the program to include a main() function and the ifmain statement.

"""

def number_classes(number=1.5):
    """states the class of the argument given"""
    #if the number given is an integer:    
    if type(number) == int:
        #print this statement
        print("the number is an integer")
    #or if the number given is a float:
    elif type(number) == float:
        #print this statement
        print("the number is a float")
    #for all the other kinds of arguments given, like strings, or lists... 
    else:
        #print this statement:
        print("not an integer nor a float, are you sure you are using a number?")

def main(number):
    number_classes(number)


if __name__ == "__main__": 
    main(1)
    main(1.5)
    main([1,2,3,4,5])
    