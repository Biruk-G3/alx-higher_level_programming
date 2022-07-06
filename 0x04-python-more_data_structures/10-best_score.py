#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None     
    
        #return max(a_dictionary, key= lambda x: a_dictionary[x])
        #return max(a_dictionary, key=a_dictionary.get)
    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            ret = k
    return (ret)
