Sample_data = {'1':['a','b'], '2':['c','d']}
#Sample_data = {'1':['a','b','c'], '2':['c','d','e'],'3':['v','f']}

list3 = []
list1 = []
list2 = []

for k, v in Sample_data.items():
    list3.append(Sample_data[k])

print(list3)

for k in range(len(list3)):
    if len(list1) == 0:
        list1.extend(list3[k])
    else:
        list2.extend(list3[k])


print('List1:',list1)
print('List2:',list2)


for i in range(len(list2)):
    for k in range(len(list1)):
        print(list1[i]+list2[k])
