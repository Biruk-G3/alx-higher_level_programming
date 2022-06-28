#!/usr/bin/python3
def uper_case(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return (ord(c) - 32)
    else:
        return ord(c)


def uppercase(string):
    string_new = ""
    for c in string:
        string_new += "%c" % uper_case(c)
    print("{:s}".format(string_new))
