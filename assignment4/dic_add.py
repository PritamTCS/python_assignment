#!/usr/bin/python
## Adding common key values in 2 dictionaries and forming a new dic
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'e':200}
d3={}
'''l=[d1,d2]
print(l)
print(d1)

for i in l:
    for j in i.keys():
        print(i)
        if j in i.keys():
            d3[j]=d1[j]+d2[j]
    
print(d3)'''
for i in d1.keys():
    if i in d2.keys():
        d3[i]=d1[i]+d2[i]
    else:
        d3[i]=d1[i]
for j in d2.keys():
    if j not in d3.keys():
        d3[j]=d2[j] 

print(d3)
