# Author: Tithy
# Date: 2026-07-18
# Description: Check whether a year is a leap year using a function.


def leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
year = int(input("Enter a year: "))
if leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} isn't a leap year.")