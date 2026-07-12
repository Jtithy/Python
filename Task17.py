# Author: Tithy
# Date: 2026-07-12
# Description: Check if a number is divisible by 5 and 11.

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11.")
elif num % 5 == 0 and num % 11 != 0:
    print("The number is divisible by only 5.")
elif num % 5 != 0 and num % 11 == 0:
    print("The number is divisible by only 11.")
else:
    print("The number isn't divisible by both 5 and 11.")