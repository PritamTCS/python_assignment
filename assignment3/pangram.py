#!/usr/bin/python
## Pangram is having all the alphabets in a given sentence
import re
#s1="The quick brown fox jumps over the lazy dog"
s1=lower(input("Enter a sentence:"))
l="abcdefghijklmnopqrstuvwxyz"
cnt=0
for i in list(l):
    if i in list(s1):
        cnt=0
    else:
        cnt += 1
        break
if cnt >0:
    print("Given string is not a pangram")
else:
    print("Given String is a pangram")     
'''if s1 == re.search(r'[a-z]+',s1):
    print("True")
else:
    print("False")'''

