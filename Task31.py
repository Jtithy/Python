# Author: Tithy
# Date: 2026-07-16
# Description: Find the LCM(Least Common Multiple) of two numbers.
# LCM = (num1*num2)/GCD


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(c, d):
    return (c*d)//gcd(c,d)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = lcm(num1, num2)
print("Least Common Multiple is: ", result)