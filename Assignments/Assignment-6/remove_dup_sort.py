new_str=''
ip_words=input("Enetr the words separated by space:\t")

word_list=[]
for word in ip_words.split(' ') :
    if word not in word_list :
        word_list.append(word)
        word_list.sort()

for phrase in word_list :
    if new_str != '' :
        new_str=new_str+' '+phrase
    else :
        new_str=phrase
print(new_str)

