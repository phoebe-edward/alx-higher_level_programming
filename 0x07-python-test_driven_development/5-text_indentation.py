#!/usr/bin/python3
"""print text with two new lines"""


def text_indentation(text):
    """after certain characters, put two new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = False
    for i, val in enumerate(text):
        if val != ' ' or flag is True:
            print("{}".format(val), end='')
            flag = True
        if val == '.' or val == '?' or val == ':':
            print()
            print()
            flag = False
