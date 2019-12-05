def intersection(first_l, sec_l):
    result = []
    for i in range(len(first_l)):
        for j in range(len(sec_l)):
            if first_l[i] == sec_l[j]:
                result.append(first_l[i])
                break
    return result
    
a = [3, 1, 4, 2]
b = [4, 5, 3, 6]
print(intersection(a, b))