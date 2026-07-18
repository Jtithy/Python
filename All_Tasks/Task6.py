#Author: Tithy
#Date: 2026-07-11
#Description: Take name as input. Check if lenght less than 3 char, print name must be at least 3 char. Otherwise if it's more than 50 char, print name can't be at most 50 char. Finally print name looks good.

name = input("Enter your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name can't be at most 50 characters.")
else:
    print("Name looks good.")