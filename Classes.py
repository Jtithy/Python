# Author: Tithy
# Date: 2026-07-14
# Description: Implementing classes in Python.

class Point:
    def move(self):
        print("Move")
        
    def draw(self):
        print("Draw")
    
point1 = Point()
point1.draw()

point1.x = 10
point1.y = 20
print(point1.x)