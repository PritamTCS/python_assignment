#!/usr/bin/python
# Accept sequence of lines and convert to uppercase and print
#text=input("Enter sequence of lines:")
#text1=text.split("\n")
#for i in text1:
#    print(i.upper())
li=[]
while True:
    text=input("Enter a line:")
    if text:
        li.append(text.upper())
    else:
        break
for i in li:
    print(i)



