#!/usr/bin/python
#script to replace the 1st charcter with $ from 2nd occurence onwards
s=input("enter a string:")
f=s[0]
s1=s.replace(f.lower(),'$')
print(s1)
print("Final string:",f+s1[1:])

