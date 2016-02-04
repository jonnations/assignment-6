#!/usr/bin/env python
# utf-8

"""
Assignment 6
Task 1 Program: Chained conditionals
Jessie Salter
2 February 2016
"""


def ays_membership(x):
    """This function assigns and print membership levels to donations"""
    if 60 <= x < 120:
        x = "Solo Membership"
    elif 120 <= x < 250:
        x = "Duet Membership"
    elif 250 <= x < 500:
        x = "Quartet Membership"
    elif 500 <= x < 1000:
        x = "Sextet Membership"
    elif 1000 <= x < 1500:
        x = "Octet Membership"
    elif 1500 <= x < 2500:
        x = "Chamber Membership"
    elif 2500 <= x < 5000:
        x = "Symphony Membership"
    elif x == 5000:
        x = "Philharmonic Membership"
    else:
        x = "generous gift"
    return x


def main():
    print("Please enter donation amount:")
    donation = int(input())
    m = ays_membership(donation)
    ty = "Thank you for your"
    print(str(ty), str(m)+"!")


if __name__ == '__main__':
    main()
