"""
Object Oriented Programming

homework 1
"""


#Problem 1 - Fill in the Line class methods to accept
#coordinates as a pair of tuples and return the slow and distance of the line.
import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return math.sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)
    
    def slope(self):
        return ((self.coor1[1] - self.coor2[1]) / (self.coor1[0] - self.coor2[0]))

#Example
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())

print(li.slope())