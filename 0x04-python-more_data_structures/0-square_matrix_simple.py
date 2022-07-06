#!/usr/bin/python3
def square_matrix_simple(matrix=[]): 
    sqr_matrix = list(map(lambda x:list(map(lambda y: (y**2), x)), matrix ))
    # number ** 2 for number in list1
    return sqr_matrix
