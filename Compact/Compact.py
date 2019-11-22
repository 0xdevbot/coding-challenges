def compact(list_in, new_list=[]):
    if len(list_in) == 0:
        return new_list
    else:
        key = list_in[0]
        new_list.append(key)
        mid = 1
        for check in list_in[1:]:
            if check != key:
                mid = list_in.index(check)
        list_out = list_in[mid:]
        return compact(list_out, new_list)



print(compact([1, 1, 2, 2, 3, 2]))

