#Author: Tithy
#Date: 2026-07-21
#Description: Calendar module demonstration.

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print("Calendar of the month", month, "of year", year, "is: \n")
print("Current month: ", cal)
print("Leap year: ", calendar.isleap(year))