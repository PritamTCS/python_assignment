def remove_duplicate(sample_list) :
    modified_list=[]
    for item in sample_list :
        if item not in modified_list :
            modified_list.append(item)
    print ("The modified list after removing the duplicates is :" ,modified_list)

remove_duplicate([[1,2],[3,4],[34],[1,2]])
remove_duplicate([[2,3,4],[2,3,4],[5],[5]])