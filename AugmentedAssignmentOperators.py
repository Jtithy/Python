#Author: Tithy
#Date: 2026-07-10
#Description: Augmented Assignment Operators in Python.
#Augmented assignment operators are a shorthand way to perform an operation on a variable and assign the result back to that variable.

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
#Sum
x += y #Equivalent to x = x+y
print("The sum of x and y is:", x)
#Sub
x -=y #x = x-y
print("The difference of x and y is:", x)
#Mul
x *= y #x = x*y
print("The product of x and y is:", x)
#Div
x /=y #x = x/y
print("The quotient of x and y is:", x)
#Mod
x %= y #x = x%y
print("The remainder of x and y is:", x)