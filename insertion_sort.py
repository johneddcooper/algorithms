def insertion_sort(input_list):
    for j in range(len(input_list)):
        key = input_list[j]
        i = j - 1
        while i > 0 and input_list[i] > key:
            input_list[i + 1] = input_list[i]
            i -= 1
        input_list[i + 1] = key
    return input_list
