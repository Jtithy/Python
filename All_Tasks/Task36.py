# Author: Tithy
# Date: 2026-07-18
# Description: Calculate the area of a circle using a function.

import math
def cal_area(radius):
    return math.pi * radius ** 2


radius = float(input("Enter the radius: "))
area = cal_area(radius)
print(f"The area of the circle is: {area:.2f}")