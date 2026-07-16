# Author: Tithy
# Date: 2026-07-16
# Description: Check if a number is a palindrome using a list.

def is_palindrome(number):
    if not number:
        return None
    number_list = list(str(number))
    reversed_list = number_list[::-1]
    return number_list == reversed_list

number = input("Enter number: ")
try:
    number = int(number)
    result = is_palindrome(number)
    print(f"The number '{number}' is a palindrome: {result}")
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

