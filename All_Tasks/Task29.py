# Author: Tithy
# Date: 2026-07-16
# Description: Print the Fibonacci series up to n terms.
#Fibonacci Series - a+b = c (Addition of previous two numbers is equal to next number)

def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a+b
    return series


number = int(input("Enter a number: "))

if number <= 0:
    print("Enter a positive number.")
else:
    fib_series = fibonacci_series(number)
    print("Fibonacci series up to ", number, "terms: ", fib_series)