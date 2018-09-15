def merge_sort(list):
    if len(list) == 1:
        return list
    newlist = []
    l_list = merge_sort(list[len(list) // 2:])
    r_list = merge_sort(list[:len(list) // 2])
    l_list_index = 0
    r_list_index = 0
    while True:
        if len(l_list) == l_list_index:
            newlist.extend(r_list[r_list_index:])
            break
        elif len(r_list) == r_list_index:
            newlist.extend(l_list[l_list_index:])
            break
        elif l_list[l_list_index] <= r_list[r_list_index]:
            newlist.append(l_list[l_list_index])
            l_list_index += 1
        elif l_list[l_list_index] > r_list[r_list_index]:
            newlist.append(r_list[r_list_index])
            r_list_index += 1
    return newlist
