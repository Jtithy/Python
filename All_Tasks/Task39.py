# Author: Tithy
# Date: 2026-07-18
# Description: Create a menu-driven calculator using functions.


def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

def mod(x, y):
    return x%y

def power(x, y):
    return x**y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")
print("7.Exit")


while True:
    choice = int(input("Enter your choice (1-7): "))
    if 1 <= choice <= 7:
        if choice == 1:
            result = add(num1, num2)
            print(f"The addition of {num1} and {num2} is: {result}")
        elif choice == 2:
            result = sub(num1, num2)
            print(f"The subtraction of {num1} and {num2} is: {result}")
        elif choice == 3:
            result = mul(num1, num2)
            print(f"The multiplication of {num1} and {num2} is: {result}")
        elif choice == 4:
            result = div(num1, num2)
            print(f"The dividion of {num1} and {num2} is: {result}")
        elif choice == 5:
            result = mod(num1, num2)
            print(f"The remainder of {num1} and {num2} is: {result}")
        elif choice == 6:
            result = power(num1, num2)
            print(f"The power of {num1} and {num2} is: {result}")
        elif choice == 7:
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Try again.")
    
        

    