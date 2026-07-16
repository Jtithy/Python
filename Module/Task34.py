# Author: Tithy
# Date: 2026-07-16
# Description: Find the largest number in a list using module.
# print(max([1, 3, 2, 5, 4])) - Python Built In Function


import Largest

numbers = input("Enter the numbers list separately (comma-separated): ").split(",")
numbers = [int(x.strip()) for x in numbers]
result = Largest.find_max(numbers)
print("The largest number is:", result)
