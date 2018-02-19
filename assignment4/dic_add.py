#!/usr/bin/python
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'e':200}
d3={}
l=[d1,d2]
print(l)
print(d1)

for i in l:
    for j in i.keys():
        print(i)
        if j in i.keys():
            d3[j]=d1[j]+d2[j]
        else:
            d3[j]=d1[j]        

print(d3)
