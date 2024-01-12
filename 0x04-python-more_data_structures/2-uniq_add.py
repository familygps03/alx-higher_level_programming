#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    product_add = 0
    for j in new_list:
        product_add += j
    return (product_add)
