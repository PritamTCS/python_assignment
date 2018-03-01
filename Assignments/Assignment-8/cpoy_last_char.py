def insert_end(ip_str) :
    slice = ip_str[-2:]
    op_str=slice*4
    print(op_str)

ip_str=input("Enter the string : ")
while len(ip_str) < 2 :
    print ("The string must be of at least two characters ")
    ip_str = input("Enter the string : \t ")
insert_end(ip_str)