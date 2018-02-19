#!/usr/bin/python
def pair(s1):
    if len(s1) >2:
        s2=s1[0:2]+s1[-2:]
        return s2
    else:
        return s1

s=input("Enter astring:")
st=pair(s)
print("First&last 2 charcters of the string is:",st)
  

