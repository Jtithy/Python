#Author: Tithy
#Date: 2026-07-12
#Description: Write a program to remove the duplicates in a list.

num = [1,2,3,1,4,2,1,4,5]
print("Original number list: ", num)

uniques = []
for number in num:
    if number not in uniques:
        uniques.append(number)
print("After removing duplicates: ", uniques)