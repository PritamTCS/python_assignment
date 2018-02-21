#!/usr/bin/python

li=[7,6,1,2,10,8,3,100,300,200,56,78,90,34,65,23,32,11,45]
#li.sort()
#l=input("Enter the list of elements:")
#li=int(l.split(","))
print(li)
s=int(input("Enter the search element:"))
f=0
l=0
def binary(A,n,x):
    f=0 
    l=n-1
    #print("Before While:",f,l,m)
    while(f<=l):
    
        m=int((f+l)/2)
        print("In While:",f,l,m)
        if x == A[m]:
            return m 
        elif x < A[m]:
            l=m-1
        else:
            f=m+1
        #return 1
    return 0 
            
    
li.sort()
print(li)
re = binary(li,len(li),s)
if re:
    print("Search element found at index:",re)
else:
    print("Search element Not Found")

