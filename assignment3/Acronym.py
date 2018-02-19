#!/usr/bin/python
#s1="Portable Network graphics"
s1=input("Enter a long name to convert to Acronym:")
f=""
l=s1.split()
print(l)
for i in l:
    f += i[0]

print(f.upper())
