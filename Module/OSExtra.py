#Author: Tithy
#Date: 2026-07-21
#Description: OS module demonstration in Python.

import os
import datetime

#Directory path
print(os.getcwd())
#Change directory
# os.chdir('\03_AllAboutPython\Python')
# print(os.getcwd())
#List of all files and directories
print(os.listdir())
#Create a new directory
# os.makedirs('OS_Demo-1/OS_Demo-2')
#Remove the directory
# os.removedirs('OS_Demo-1/OS_Demo-2')
#Rename file or directory
#os.rename('text.txt', 'demo.txt')
#Get the status of a file or directory
print(os.stat('All_Tasks'))
#Status in bytes
print(os.stat('All_Tasks').st_size)

#Get the last modified time of a file or directory
mod_time = os.stat('All_Tasks').st_mtime
#Convert the time in seconds to a readable format
print(datetime.datetime.fromtimestamp(mod_time))

#Traverse the directory tree
for dirpath, dirnames, filenames in os.walk('All_Tasks'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

#Get environment information
print(os.environ.get('All_Tasks'))

# print(os.path.join(os.environ.get('All_Tasks'), 'text.txt'))