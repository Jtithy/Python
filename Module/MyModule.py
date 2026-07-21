#Author: Tithy
#Date: 2026-07-21
#Description: Module demonstration.

print("Imported MyModule...")

text = 'Test String'

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return -1
