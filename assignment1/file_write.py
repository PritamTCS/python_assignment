import re
li = []
while True: 
    string = input("Enter a string:")
    if string == " ":
        break
    else:
	li.append(string)

print(li)
li.sort()
print(li)

word=input("Enter a Alphanumeric word:")
#if word.isalnum():
if re.match('^[a-zA-Z0-9]+$',word):
    print(word)
    lis=list(word)
    cnt_l=cnt_w=0
    for i in lis:
        print(i)
        if i.isdigit():
            cnt_w += 1
        else:
            cnt_l += 1
else:
    print("Not an alphanumeric word")

print("Count of digits and letters:",cnt_w,cnt_l)
   
    

