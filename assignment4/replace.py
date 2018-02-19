#!/usr/bin/python
s=input("enter a string:")
f=s[0]
s1=s.replace(f.lower(),'$')
print(s1)
print("Final string:",f+s1[1:])

