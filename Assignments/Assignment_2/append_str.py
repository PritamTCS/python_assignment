#! /usr/bin/python3

def append_items(strng,ip_list) :
    new_list=[]
    for item in ip_list :
        res_op = strng + str(item)
        new_list.append(res_op)
    print (new_list)

append_items('abc',[1,2,3,4])