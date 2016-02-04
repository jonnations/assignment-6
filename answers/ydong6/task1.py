'''
Created on Feb 4, 2016

@author: York
'''
def task1(num):
        
    if num <= 10: 
        #mySum += num 
        num += 1  
        print(num)
    elif 10<num<=20 :
        print("bigger")
    else:
        print("invalid")
    return num

def main():
    
    a=task1(num=int(input('enter:')))
    print('a=',a)
    
if __name__ == '__main__':
   main()
        