#!/usr/bin/python
def func():
    pass

def func1(arg):
    return arg

def func2(*arg):
    for i in arg:
        print(i)
def func3(def1='10',*args,**kwargs):
    #for key,value in kwargs.items():
       # print("key values are",key+ '->'+ value,def1)
     print(def1,args,kwargs)

def add(num):
    return num

print(func())
print("func1:",func1("Hi"))
print("func2:",func2('Hello','How are you','Bye'))
dic={'name':'Ramya','company':'Tcs','Project':'Nexgen'}
#print("func3:",func3(name='Ramya',ID='1072994'))
#print("func3:",func3(name='Ramya',ID='1072994'))
l1=(1,2,3)
print(func3(20,l1,name='Ramya',ID='1072994'))
i=10
print(add(100))

