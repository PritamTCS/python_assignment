#!/usr/bin/python
## Script to form numbers from given digits
l=input("enter digits to form numbers:")
li=l.split(",")
print(len(li))
#while(len(l) > x):
for i in range(0,len(li)):
    for j in range(0,len(li)):
        for k in range(0,len(li)):
            if(i!=j&j!=k&k!=i):
                print(li[i]+li[j]+li[k])




      
