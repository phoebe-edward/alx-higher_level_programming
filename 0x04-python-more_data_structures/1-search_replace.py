#!/usr/bin/python3
def search_replace(my_list, search, replace):
    length = len(my_list)
    if length == 0:
        return my_list
    new_list = []
    for i in range(length):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return new_list
