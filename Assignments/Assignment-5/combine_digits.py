def generate_comb (no_1st,no_2nd,no_3rd):
    d=[]
    d.append(no_1st)
    d.append(no_2nd)
    d.append(no_3rd)

    for i in range(0,3) :
        for j in range(0,3) :
            for k in range(0,3) :
                if (i!=j & j!=k & i!=k) :
                    print (d[i],d[j],d[k])

first=int(input("Enter the first number : \t"))
second=int(input("Enter the second number : \t"))
third=int(input("Enter the 3rd number :\t"))

generate_comb(first,second,third)