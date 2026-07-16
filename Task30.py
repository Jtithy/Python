# Author: Tithy
# Date: 2026-07-16
# Description: Find the GCD(Greatest Common Divisor) of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)
print("Greatest Common Divisor is: ", result)