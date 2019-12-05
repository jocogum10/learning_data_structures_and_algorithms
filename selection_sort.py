def selection_sort(my_list):
    for curr_index in range(len(my_list)):                          # pass through all the index of the list
        lowest_number_index = curr_index                            # set lowest number to current index
        for next_index in range(curr_index, len(my_list)):          # pass through all the list value starting from the next index
            if my_list[next_index] < my_list[lowest_number_index]:  # compare if value at next index is lesser than the current index
                lowest_number_index = next_index                    # set lowest number to next index
        if lowest_number_index != curr_index:                       # if the lowest number is not the current index    
            my_list[curr_index], my_list[lowest_number_index] = my_list[lowest_number_index], my_list[curr_index]   # swap the value of the current index to the lowest number
    return my_list
        
a = [4, 2, 7, 3, 1, 10, 29, 5, 6, 18, 8]
print(selection_sort(a))