#!/usr/bin/python
li=[(2,5,1),(1,2,3),(4,4,6),(2,3,2),(2,1,9)]
def tup_last(tp):
    print(len(tp)-1)
    print(tp[len(tp)-1])
    return tp[len(tp)-1]
li.sort(key=tup_last)
print(li)

'''for i in li:
    li.sort(key=i[len(i)-1])

print(li)'''
