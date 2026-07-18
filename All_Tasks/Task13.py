#Author: Tithy
#Date: 2026-07-12
#Description: Write a program to find the largest number in a list.

numbers = [2,4,12,54,23]
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest number: ", largest)