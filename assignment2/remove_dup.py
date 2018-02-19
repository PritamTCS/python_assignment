#!/usr/bin/python

li=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
uniq=[]
for i in li:
    if i not in uniq:
        uniq.append(i)

print(uniq)
