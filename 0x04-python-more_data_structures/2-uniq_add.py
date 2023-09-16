#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    length = len(my_list)
    if length == 0:
        return sum
    new_list = set(my_list)
    for i in new_list:
        sum += i
    return sum
