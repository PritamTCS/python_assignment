#!/usr/bin/python
# Script to remove duplicate words from a given sentence
text=input("enter some text:")
text1=text.split(" ")
text1=set(text1)
text_dup=" ".join(text1)
print(text_dup)

