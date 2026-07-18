# Author: Tithy
# Date: 2026-07-16
# Description: Check whether a number is an Armstrong number.
#An Armstrong number is a number that is equal to the sum of its digits, where each digit is raised to the power of the total number of digits.

def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    
    return sum_of_powers == num

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "isn't an Armstrong number.")

