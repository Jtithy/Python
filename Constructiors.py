# Author: Tithy
# Date: 2026-07-14
# Description: Constructors in Python.
#Constructors are special methods that are automatically called when an object is created. In Python, the constructor method is defined using the __init__() method. It allows you to initialize the attributes of an object when it is created.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        print("Move")
        
    def draw(self):
        print("Draw")
    
point = Point(10, 20)
print(point.x)
print(point.y)