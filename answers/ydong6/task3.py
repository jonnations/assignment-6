
'''
Created on Feb 3, 2016

@author: York
'''
import functools
def Euler(n=1,x=1):
    i= 1
    together=[]

    while n <= x:
      
        i = i * n
        """recursion"""
        n=n+1
        #Euler(n=n+1)
        #Euler(n=1,x=1)
        together.append(1/i)
        #print(together)
        list=(functools.reduce(lambda z, y: z+y,together))
    
        #print(together)
        
    else:
        print("At least i tried!")
        return list
def main():
     e=Euler(n=1,x=1000)
     print(e+1)
if __name__ == "__main__":
    main()