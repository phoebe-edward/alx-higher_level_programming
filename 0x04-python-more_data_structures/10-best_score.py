#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    max_k = list(a_dictionary)[0]
    max_v = a_dictionary[max_k]
    for k, v in a_dictionary.items():
        if v > max_v:
            max_k = k
            max_v = v
    return max_k
