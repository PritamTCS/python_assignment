#!/usr/bin/python
num=input("Enter a number:")
am=0
l=len(str(num))
for i in list(str(num)):
    am +=int(i)**l
print(am)
if am == num:
    print("Given number is amstrong number")
else:
    print("Not an amstrong number")



