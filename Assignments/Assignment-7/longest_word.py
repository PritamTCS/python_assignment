word_dict={}
longest_word_list=[]
final_list=''

with open("/home/tcs/PycharmProjects/python_practice/assignment_1/datafile","r") as fr :
    for line in fr :
        line=line.rstrip('\n')
        for word in line.split(' '):
            word_dict[word]=len(word)

fr.close()

value_list=word_dict.values()
max_len=max(value_list)

for key in word_dict :
    if word_dict[key] == max_len :
        longest_word_list.append(key)

for wrd in longest_word_list :
    if final_list != '' :
        final_list = final_list+','+wrd
    else :
        final_list = wrd

print("Longest word in the file : " , final_list)
