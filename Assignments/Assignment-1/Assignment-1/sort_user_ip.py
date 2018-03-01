def sort_ip_lines(strng):
    word_list=strng.split(' ')
    sorted_word_list=sorted(word_list)
    fw=open("/home/tcs/PycharmProjects/python_practice/assignment_1/op_file","w")
    fw.write(str(sorted_word_list))
    print ("Output can be checked in 'op_file' in the '/home/tcs/PycharmProjects/python_practice/assignment_1' path ")

def count_alp_num(str) :
    alphbt=0
    digit=0
    for i in str :
        if (i.isalpha()) :
            alphbt += 1
        elif (i.isnumeric()) :
            digit += 1
    print (" Number of alphabets in the input string is :" , alphbt)
    print(" Number of digits in the input string is :", digit)

ip_str=input("Please provide the input lines : \t")
sort_ip_lines(ip_str)
alp_num_str=input("Enter an alphanumeric string : \t")
count_alp_num(alp_num_str)