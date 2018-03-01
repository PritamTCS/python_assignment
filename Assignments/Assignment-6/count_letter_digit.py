def count(sentence) :
    alp_count = 0
    dig_count = 0
    for i in sentence :
        if (i.isalpha()) :
            alp_count += 1
        elif (i.isnumeric()) :
            dig_count += 1
    return alp_count,dig_count

ip_sentence=input("Enter the sentence: \t")

cnt_ltr,cnt_num=count(ip_sentence)
print ("LETTERS " , cnt_ltr)
print ("DIGITS ", cnt_num)
