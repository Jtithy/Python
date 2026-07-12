#Author: Tithy
#Date: 2026-07-12
#Description: Implementing list methods in Python.

num = [3, 2, 4, 5, 1]
print("Original: ", num)
num.append(10)
print("After inserting: ", num)
num.insert(3, 13)
print("After inserting at index 3: ", num)
num.remove(4)
print("After removing 4: ", num)
num.pop()
print("After popping: ", num)
num.sort()
print("After sorting: ", num)
num.reverse()
print("After reversing: ", num)
num2 = num.copy()
print("Copied list: ", num2)

# num.clear()