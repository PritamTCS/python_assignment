def form_array(no1,no2) :
    main_arr=[]
    for i in range(0, no1):
        arr_i = []
    for i in range(0,no1) :
        arr=[]
        for j in range(0,no2) :
            #print(i,j)
            #print(j)
            arr.append(i*j)
            #arr_i[j]=i*j
            #print(j)
        main_arr.append(arr)
    print(main_arr)
    #print (arr)
no1=int(input("Enter the first number : "))
no2=int(input("Enter the second number : "))

form_array(no1,no2)