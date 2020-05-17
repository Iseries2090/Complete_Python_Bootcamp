"""
File I/O

This exercise will require several lines of code

Write a script that opens a file named 'test.txt', writes 'hello world' to the file and then closes it.

"""

x = open('test.txt','w')
x.write('Hello World')
x.close()