#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1 = set_1 - set_2
    set2 = set_2 - set_1
    return list(set1.union(set2))
