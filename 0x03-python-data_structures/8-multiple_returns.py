#!usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        character = None
    else:
        character = sentence[0]
    return (length, character)
