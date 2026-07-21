#Author: Tithy
#Date: 2026-07-10
#Description: Importing MyModule.py here.


import MyModule
import sys

courses = ['Math', 'Science', 'Physics', 'History', 'English']
print("Courses list: ", courses)

option = input('Select a course from the list: ')
index = MyModule.find_index(courses, option)
print(index)
print("Module Path: ", sys.path)