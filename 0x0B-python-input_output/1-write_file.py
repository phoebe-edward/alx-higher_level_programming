#!/usr/bin/python3
"""write into txt file"""


def write_file(filename="", text=""):
    """write into file"""
    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
        return num
