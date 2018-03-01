ip_nos=input("Enter the numbers separated by comma:\t")

list=[]

for i in ip_nos.split(','):
    list.append(i)

tup=tuple(list)

print ("The given numbers in list format:\t",list)
print ("The given numbers in tuple format:\t",tup)