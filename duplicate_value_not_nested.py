steps = 0
def has_duplicate_value_array(my_list):
    global steps
    existing_numbers = []
    for i in range(len(my_list)):
        steps += 1
        if (my_list[i] not in existing_numbers):
            existing_numbers.append(my_list[i])
        else:
            return True
    return False
    
l = [1, 2, 3, 4, 5, 9, 10]
a = has_duplicate_value_array(l)
print("duplicate: {0}, steps: {1}".format(a, steps))