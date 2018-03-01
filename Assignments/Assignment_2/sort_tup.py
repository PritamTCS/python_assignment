def sort_tup (ip_list) :
    last_element_list=[]
    repo_dict={}
    final_list=[]
    for tpl in ip_list :
        #for item in tpl :
        last_element=tpl[-1]
        if last_element not in last_element_list :
            last_element_list.append((last_element))
    sorted_op_list=sorted(last_element_list,reverse = True)
    for item in sorted_op_list :
        for tpl in ip_list :
            last_element = tpl[-1]
            if (item == last_element) :
                final_list.append(tpl)
    print (final_list)



    """if last_element in repo_dict :
            repo_dict[last_element] = str((repo_dict[last_element])) + ';' + str(tpl)
        else :
            repo_dict[last_element]=tpl
        #print (repo_dict)

    for key in sorted_op_list :
        if ';' not in repo_dict[key] :
            final_list.append(repo_dict[key])
        else:
            for value in repo_dict[key].split(';') :
                final_list.append(value)
    print (final_list)
    for item in final_list :
        print (type(item))"""




sort_tup ([(1,2),(3,4),(6,9),(7,9),(8,9)])
sort_tup ([(9,),(2,3,4),(3,4)])