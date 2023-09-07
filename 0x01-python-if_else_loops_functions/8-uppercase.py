#!/usr/bin/python3
def uppercase(str):
    new_str = ''
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            new_str += chr(ord(i) - 32)
        else:
            new_str += i
    print("{:s}".format(new_str))
