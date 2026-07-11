#Author: Tithy
#Date: 2026-07-10
#Description: Implementing logical operators in Python.
#Logical Operators: AND(All statements are true), OR(At least one statement is true), NOT(Reverse the statement)

has_high_income = input("Do you've a high income? (T/F): ")
has_good_credit = input("Do you've good credit? (T/F): ")

if has_high_income == "T" and has_good_credit == "T":
    print("Eligible for loan.")
else:
    print("Not eligible for loan.")

has_good_CGPA = input("Do you've a good CGPA? (T/F): ")
has_criminal_record = input("Do you've a criminal record? (T/F): ")

if has_good_CGPA == "T" or has_criminal_record =="F":
    print("Eligible for scholarship.")
else:
    print("Not eligible for scholarship.")

selected = input("Are you selected? (T/F): ")
if selected != "T":
    print("Not selected.")
elif selected != "F":
    print("Selected.")