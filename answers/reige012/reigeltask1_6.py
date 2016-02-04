#!/usr/bin/env python
# #encoding: utf-8

"""
Program made using chained conditionals. The purpose of this program is to use
the variable age as the age of the person and give a different output depending
on how old they are.

Created by Alicia Reigel. 3 February 2016.
Copyright Alicia Reigel. Louisiana State University. 3 February 2016.

"""

def your_age(arg1):
    """this function takes someone's age and gives them an upbeat feedback"""
    x=arg1
    if x<=12:
        print("Age:", end="")
        print(x)
        print("Hey, you're a cool kid!")
    elif (x>12) and (x<=19):
        print("Age:", end="")
        print(x)
        print("Hey, teenagers are pretty great!")
    elif (x>19) and (x<=30):
        print("Age:", end="")
        print(x)
        print("Your twenties are the best years of your life! ")
    elif (x>30) and (x<=50):
        print("Age:", end="")
        print(x)
        print("You're not old yet...so enjoy life a little!")
    elif (x>50):
        print("Age:", end="")
        print(x)
        print("Hey, you might be old, but you're still cool!")

def main():
    #I put one of each age category here to show how it works. Ideally there would only be one your_age() found in the main function.
    your_age(3)
    your_age(14)
    your_age(25)
    your_age(39)
    your_age(57)

if __name__ == '__main__':
        main()
