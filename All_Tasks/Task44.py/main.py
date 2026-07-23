#Author: Tithy
#Date: 2026-07-23
#Description: Create your own package containing at least three modules in Python.

# main.py

from math_utils import add, subtract, multiply

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))