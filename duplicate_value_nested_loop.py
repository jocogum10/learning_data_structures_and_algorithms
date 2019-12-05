steps = 0
def has_duplicate_value_array(my_list):
    global steps
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            steps += 1
            if(i != j and my_list[i] == my_list[j]):
                return True
    return False
    
l = [1, 2, 3, 4, 5]
a = has_duplicate_value_array(l)
print("steps: {0}, has duplicate: {1}".format(steps, a))