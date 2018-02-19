#!/usr/bin/python
inp=input("Enter the string:")
li=list(inp)
print(li[::-1])
li.reverse()
rever="".join(li)

print(rever)

if inp == rever:
    print("Given string is a palindrome")
else:
    print("Given string is not palindrome")



