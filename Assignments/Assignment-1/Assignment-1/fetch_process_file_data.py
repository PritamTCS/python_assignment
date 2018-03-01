word_freq={}
word_len={}
with open("/home/tcs/PycharmProjects/python_practice/assignment_1/datafile","r") as fr :
    for line in fr:
        print(line.title())
        print ("\n")
        wrd_list=line.split()
        for word in wrd_list :
            if word in word_freq :
                word_freq[word] += 1
            else:
                word_freq[word] = 1
            w_len=len(list(word))
            word_len[word] = w_len

print ("Frequency of each word in the file :")
print (word_freq)
print ("Length of each word in the file :")
print (word_len)




