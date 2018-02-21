#!/usr/bin/python
import re
cnt_l=cnt_w=0
word=input("Enter a Alphanumeric word:")
#if word.isalnum():
if re.match('^[a-zA-Z0-9]+$',word):
    print(word)
    lis=list(word)
    for i in lis:
        if i.isdigit():
            cnt_w += 1
        else:
            cnt_l += 1
else:
    print("Not an alphanumeric word")

print("Count of digits and letters:",cnt_w,cnt_l)
