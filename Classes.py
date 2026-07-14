# Author: Tithy
# Date: 2026-07-14
# Description: Implementing classes in Python.

class Point:    
    def move(self):
        print("Move")
        
    def draw(self):
        print("Draw")
    
point = Point()
point.x = 10
point.y =20
print(point.x)
print(point.y)