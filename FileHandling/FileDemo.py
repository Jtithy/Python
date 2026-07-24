#Author: Tithy
#Date: 2026-07-24
#Description: Program to demonstrate file handling in Python.


import os
#File directory path
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "text.txt")

#Read file content
f = open(file_path, "r")

print("File Name: ", f.name)
print("File Mode: ", f.mode)

#Close the file
f.close()

#Context manager to read file content
with open(file_path, "r") as f:
    content = f.read()
    print("File All Content: ")
    print(content)
    
    pass
    

