ip_str=input("Enter the string : ")
index_ch=input("Enter the index and character to replace separated by comma :")

index,ch=index_ch.split(',')
index=int(index)
list_obj=list(ip_str)
list_obj[index]=ch
new_str=''.join(str(item) for item in list_obj)
print(new_str)
