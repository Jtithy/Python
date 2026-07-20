#Author: Tithy
#Date: 2026-07-20
#Description: Working with directories and files in Python.
#On Windows: c:\Program Files\Microsoft
#ON Mac: /users/local/bin

from pathlib import Path
#Absolute path
#Relative path

# path = Path('emails')
# print(path.mkdir()) #Create directory
# print(path.rmdir()) #Remove/Delete directory

path = Path()
for file in path.glob('*.py'): #List all files with .py
    print(file)

