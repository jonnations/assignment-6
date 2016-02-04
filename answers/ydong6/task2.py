'''
Created on Feb 2, 2016

@author: York
Task 2

Write a program that uses a recursive function to compute the sum of the integers from 0 to 1000 (inclusive). Return the sum of these numbers to the main loop and print the result. Write the program to include a main() function and the ifmain statement.
'''
def mySum():
    mySum = 0 
    num = 1 
    
    while num <= 1000: 
        mySum += num 
        num += 1   
       
    #print (mySum)
    return mySum

def main():
    a=mySum()
    print('a=',a)
if __name__ == '__main__':
   main()
        