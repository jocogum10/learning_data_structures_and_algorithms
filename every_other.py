def every_other(my_list):
    new_list = []
    for i in range(0, len(my_list), 2):
        new_list.append(my_list[i])
    return new_list
    
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(every_other(a))