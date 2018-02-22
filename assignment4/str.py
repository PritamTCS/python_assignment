#!/usr/bin/python
## extracting first& last 2 charcter from a given string
def pair(s1):
    if len(s1) >2:
        s2=s1[0:2]+s1[-2:]
        #return s2
        print("First&last 2 charcters of the string is:",s2)
    else:
        #return ""
        print("length of string is less than 2")

s=input("Enter a string:")
st=pair(s)
#print("First&last 2 charcters of the string is:",st)
  

