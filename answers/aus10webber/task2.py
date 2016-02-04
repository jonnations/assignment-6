#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 6, Task 2
Austen T. Webber
2016_2_2
"""

# Find sum of integers from 0 to 1000

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum(range(1,1000)))

if __name__ == '__main__':
  listsum()

# http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html
