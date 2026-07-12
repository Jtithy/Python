#Author: Tithy
#Date: 2026-07-12
#Description: Implementing for loop in Python.
#Use to iterate over items of a collection

#Iteration over a string
print("'Python' String iteration: ")
for item in 'Python':
    print(item)
    
#List of items
print("List iteration: ")
for item in ['Python', 'Java', 'C++']:
    print(item)
    
#Range function
print("Range function: ")
for item in range(2):
    print(item)
#Range function with start and end
print("Range function with start and end: ")
for item in range(-3, 2):
    print(item)

#Range function with start, end and step
print("Range function with start, end and step: ")
for item in range(-10, 10, 2):
    print(item)