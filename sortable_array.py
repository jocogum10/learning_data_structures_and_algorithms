class SortableArray:
    def __init__(self, array):
        self.array = array
        
    def partition(self, left_pointer, right_pointer):
        pivot_position = right_pointer              # choose right most index as the pivot
        pivot = self.array[pivot_position]
        
        right_pointer -= 1
        
        while True:
            while self.array[left_pointer] < pivot:
                left_pointer += 1
            while self.array[right_pointer] > pivot:
                right_pointer -= 1
            
            if left_pointer >= right_pointer:                               # if left_pointer points is at same index as right pointer or index+1
                break
            else:
                self.swap(left_pointer, right_pointer)
        
        self.swap(left_pointer, pivot_position)
        
        return left_pointer
        
    def swap(self, pointer_1, pointer_2):
        self.array[pointer_1], self.array[pointer_2] = self.array[pointer_2], self.array[pointer_1]
        
    def quicksort(self, left_index, right_index):
        if (right_index - left_index) <= 0:                                 # base case
            return
            
        pivot_position = self.partition(left_index, right_index)            # partition the array and grab the position of the pivot
        self.quicksort(left_index , pivot_position - 1)                     # recursively call this quicksort method on whatever is to the left of the pivot
        self.quicksort(pivot_position + 1, right_index)                     # recursively call this quicksort method on whatever is to the right of the pivot
        
    def quickselect(self, kth_lowest_value, left_index, right_index):
        if (right_index - left_index) <= 0:                                 # base case
            print(self.array[left_index])
        
        pivot_position = self.partition(left_index, right_index)            # partition the array and grab the position of the pivot
        
        if kth_lowest_value < pivot_position:                               # search value on the left of the pivot
            self.quickselect(kth_lowest_value, left_index, pivot_position-1)
        elif kth_lowest_value > pivot_position:                             # search value on the right of the pivot
            self.quickselect(kth_lowest_value, pivot_position+1, right_index)
        else:                                                               # if kth_lowest_value == pivot position
            print(self.array[pivot_position])
            
        
if __name__ == '__main__':
    array = [0, 5, 2, 1, 6, 3]
    sortable_array = SortableArray(array)
    sortable_array.quicksort(0, len(array)-1)
    print(sortable_array.array)
    
    new_array = [0, 50, 20, 10, 60, 30]
    sorted_array = SortableArray(new_array)
    sorted_array.quickselect(1, 0, len(new_array)-1)