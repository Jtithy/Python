# Author: Tithy
# Date: 2026-07-12
# Description: Check if a triangle is valid from its three angles.

angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

if angle1 > 0 and angle2 > 0 and angle3 > 0:
    if angle1 + angle2 + angle3 == 180:
        print("The triangle is valid.")
    else:
        print("The triangle is invalid.")
else:
    print("Triangle angles must be greater than 0.")