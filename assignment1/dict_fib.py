#!/usr/bin/perl
num=int(input("Enter a number:"))
if num == 0:
    b=[]
elif num == 1:
    b=[1]
elif num == 2:
    b=[1,1]
elif num > 2:
    dic={1:1,2:1}
    for i in range(3,num+1):
        dic[i]=dic[i-2]+dic[i-1]
    b=dic.values()
print(b)
    
    
 

