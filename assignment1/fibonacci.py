#!/usr/bin/python 
## Fibonacci series for a given number

num = int(input("enter a number :")) 
i=1
if num == 0:
   b=[]

elif num == 1:
    b=[1]

elif num == 2:
    b=[1,1]

elif num > 2:
    b=[1,1]
    while i < (num-1):
        b.append(b[i] + b[i-1])
        i += 1
    print(b)
