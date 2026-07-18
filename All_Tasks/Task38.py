# Author: Tithy
# Date: 2026-07-18
# Description: Sort a list without using sort().

list = [5, 2, 7, 34, 1, 0, 23]

for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[i]:
            list[j], list[i] = list[i], list[j]
            
print("Sorted list: ", list)