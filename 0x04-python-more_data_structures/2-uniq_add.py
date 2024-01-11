#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    for num in my_list:
        unique_set.add(num)
    result = sum(unique_set)
    return result
my_list = [1, 2, 3, 2, 4, 5, 1, 6]
result = uniq_add(my_list)
print(result)
