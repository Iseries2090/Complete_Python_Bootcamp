"""
Functions #10: Skyline

Define a function called myfunc that takes in a string, and returs a matching
string where every even letter is uppercase, and every odd letter is lowercase.
Assume that the incoming string only contains letters, and don't worry about numbers,
spaces or punctuation.  The ouput string can start with either an uppercase or lowercase letter,
so long as letters alternate throughout the string.

"""

def myfunc(mystring):
    output = ''
    mystring = mystring.lower()
    for x in range(0,(len(mystring))):
        if x % 2 == 0:
            output += mystring[x].upper()
        else:
            output += mystring[x]
    return output

#test solution
print(myfunc('barnyard'))