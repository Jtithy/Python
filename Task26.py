# Author: Tithy
# Date: 2026-07-16
# Description: Create a dictionary to store employee information and display it.


def emp_dictionary():
    employee = {
        "name": input("Enter employee name: "),
        "age": int(input("Enter employee age: ")),
        "email": input("Enter employee email: "),
        "department": input("Enter employee department: "),
        "salary": float(input("Enter employee salary: "))
    }
    return employee

def display_info(employee):
    print("\nEmployee information:")
    for key, value in employee.items():
        print(f"{key.capitalize()}:{value}")


#Calling functions
employee = emp_dictionary()
display_info(employee)