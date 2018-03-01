comb_str=input("Enter the strings separated by space :")
str1,str2=comb_str.split(' ')

print (str1,str2)

new_str1=str2[0:2]+str1[2:]
new_str2=str1[0:2]+str2[2:]
print("Strings after modification :" ,new_str1,new_str2)