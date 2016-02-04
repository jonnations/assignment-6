import argparse
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
        print("I tried!")
        return list 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The Euler number" + "you wish to calculate", type=int)
    args = parser.parse_args()
    e=Euler(n=1,x=int(args.num))
    print(e+1)
    
    
if __name__ == "__main__":
        main()
        