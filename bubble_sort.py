def bubble_sort(list):
    unsorted_until_index = len(list) - 1                # keep track of up to which index is still unsorted
    sorted = False                                      # keep track wheter the array is fully sorted
    
    while not sorted:
        sorted = True                                   # set sorted to True if we have not made any swaps during the for loop
        for i in range(unsorted_until_index):           # loop from start of index until the unsorted index
            if list[i] > list[i+1]:                     # compare every index and the next index
                sorted = False                          # if there is swapping, sorted is False
                list[i], list[i+1] = list[i+1], list[i] # if index is greater than next index, swap the values
        unsorted_until_index = unsorted_until_index - 1 # decrement the unsorted index by 1 since we know during first passthrough, last index is already sorted
        
list = [65, 55, 45, 35, 25, 15, 10]
bubble_sort(list)
print(list)