# Author: Tithy
# Date: 2026-07-16
# Description: Find the largest number in a list using module.

import Largest

numbers = input("Enter the numbers list separately (comma-separated): ").split(",")
numbers = [int(x.strip()) for x in numbers]
result = Largest.find_max(numbers)
print("The largest number is:", result)
