ip_str=input("Enter the string : ")

ip_list=list(ip_str)

count=len(ip_list)

for i in range(0,count) :
    if i%2 != 0 :
        ip_list[i]=''

new_str=''.join(str(item) for item in ip_list)
print(new_str)
