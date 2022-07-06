#!/usr/bin/python3
def roman_to_int(roman_string):
       
    if (not isinstance(roman_string, str) or roman_string is None) :
         return (0)
    roman_dict = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500, "M": 1000 }
    num = 0
    last = "I"
    for x in roman_string[::-1]:
        if roman_dict[x] < roman_dict[last]:
            num -= roman_dict[x]
        else:
            num += roman_dict[x]
        last = x 
    return num
