#!/usr/bin/python

X=input("enter the row value:")
Y=input("enter the column value:")
two_dim = [[0 for j in range(int(Y))] for i in range(int(X))]
print(two_dim)
[[i * j for j in range(int(X))] for i in range(int(Y))]

for i in range(int(X)):
    for j in range(int(Y)):
        two_dim[i][j]= i*j

print(two_dim)
'''for i in range(X):
    for j in range(Y):
   '''     
