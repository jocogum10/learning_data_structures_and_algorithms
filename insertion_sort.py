def insertion_sort(my_list):
    for index in range(1, len(my_list)):                            # pass through the list starting at index 1
        position = index                                            # current index is stored in the position
        temp_value = my_list[index]                                 # value at the current index is stored in temp value
        while position > 0 and my_list[position-1] > temp_value:    # while the current index is not the index 0, and value to the left of current index greater than the temp value
            my_list[position] = my_list[position-1]                 # shift the value of left of current index to the current index
            position -= 1                                           # decrement the current index
        my_list[position] = temp_value                              # store the temp value to the current index
    return my_list
        
a = [4, 2, 7, 3, 1, 10, 29, 5, 6, 18, 8]
print(insertion_sort(a))