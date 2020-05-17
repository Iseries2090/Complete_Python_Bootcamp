"""
Functions #9: Pick Evens

Define a function called myfunc that takes in an arbitrary number of arguments, and
returns a list containing only those arguments that are even

"""

def myfunc(*args):
    output = []
    for elem in args:
        if elem % 2 == 0:
            output.append(elem)
    return output