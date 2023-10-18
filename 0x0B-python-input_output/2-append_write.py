#!/usr/bin/python3
"""append into txt file"""


def append_write(filename="", text=""):
    """append into file"""
    with open(filename, 'a', encoding="utf-8") as f:
        num = f.write(text)
        return num
