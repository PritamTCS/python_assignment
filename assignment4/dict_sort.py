#!/usr/bin/python
dic={'Math':81,'Pysics':83,'Chemistry':87}
li=[]
'''for key,value in dic.items():
    t=(key,value)
    li.append(t)
'''
##List comprehension
li=[(key,value) for key,value in dic.items()]
print(li)

def tup_last(tp):
    return tp[len(tp)-1]
##Sorting in descending order
li.sort(key=tup_last,reverse=True)
print(li)

