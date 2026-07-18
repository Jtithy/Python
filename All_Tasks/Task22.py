# Author: Tithy
# Date: 2026-07-16
# Description: Find the largest and smallest numbers in a list without using max() or min().


def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest

def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
    return smallest

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
largest_Number = find_largest(numbers)
smallest_Number = find_smallest(numbers)

print("Largest number is: ", largest_Number)
print("Smallest number is: ", smallest_Number)