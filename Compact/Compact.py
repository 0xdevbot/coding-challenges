def compact(list_in, new_list=[]):
    '''
    The purpose of this method is to take a input list of numbers and compact the list down, any recurring numbers
    that also are agasent will be reduced to a single number
    EXAMPLE: [1, 1, 2, 2, 3, 2] -> [1,2,3,2]
    :param list_in: List of numbers to be inputted by the user
    :param new_list: this is the new list that the method creates
    :return:  BASE CASE: returns new_list which contains the final output, the output is iter
    '''
    if len(list_in) == 0:
        return iter(new_list)
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



