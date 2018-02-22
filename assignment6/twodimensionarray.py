#!/usr/bin/python

X=input("enter the row value:")
Y=input("enter the column value:")
## creating a dummy 2D array
two_dim = [[10 for j in range(int(Y))] for i in range(int(X))]
print(two_dim)
## Resetting with actual values
for i in range(int(X)):
    for j in range(int(Y)):
        two_dim[i][j]= i*j

print(two_dim)
