#!/usr/bin/python
words=[]
dic={}
f=open("/home/tcs/Desktop/Python_Practice/assignment1/sampl.txt","r")
for line in f:
    words=line.split(" ")
    for i in words:
        print("length of word is:",str(i).capitalize(),len(i))
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

print(dic) 
