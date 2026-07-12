# Author: Tithy
# Date: 2026-07-12
# Description: Implement a program that takes a phone number and returns the spelling of each digit.
#Task 15 in different way
phone = input("Phone: ")

while not phone.isdigit() or len(phone) != 11:
    if not phone.isdigit():
        print("Invalid input. Digits only.")
    elif len(phone) != 11:
        print("Invalid phone number. It must contain 11 digits.")
    phone = input("Phone: ")

for digit in phone:
    if digit == '0':
        print("Zero")
    elif digit == '1':
        print("One")
    elif digit == '2':
        print("Two")
    elif digit == '3':
        print("Three")
    elif digit == '4':
        print("Four")
    elif digit == '5':
        print("Five")
    elif digit == '6':
        print("Six")
    elif digit == '7':
        print("Seven")
    elif digit == '8':
        print("Eight")
    elif digit == '9':
        print("Nine")