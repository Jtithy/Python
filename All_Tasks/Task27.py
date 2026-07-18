# Author: Tithy
# Date: 2026-07-16
# Description: Create a dictionary to store employee information while handling errors and display it.


def emp_dictionary():
        #Validate name
        while True:
            try:
                name = input("Enter your name: ")
                if not name.isalpha():
                    raise ValueError("Name must be alphabetic.")
                break
            except ValueError as e:
                print(e)
            
        #Validate age
        while True:
            try:
                age = int(input("Enter your age: "))
                if age <= 0:
                    raise ValueError("Age must be a positive integer.")
                break
            except ValueError as e:
                print(e)
        
        #Validate email
        while True:
            try:
                email = input("Enter your email: ")
                if "@gmail.com" not in email:
                    raise ValueError("Invalid email format.")
                break
            except ValueError as e:
                print(e)
        
        #Validate department
        while True:
            try:
                department = input("Enter your department: ")
                if not department.isalpha():
                    raise ValueError("Department must be alphabetic.")
                break
            except ValueError as e:
                print(e)
                
        #Validate salary
        while True:
            try:
                salary = int(input("Enter your salary: "))
                if salary <= 0:
                    raise ValueError("Salary must be a positive integer.")
                break
            except ValueError as e:
                print(e)
                
                
        employee = {
            "name" : name,
            "age" : age,
            "email" : email,
            "department" : department,
            "salary" : salary
        }
        
        return employee 
    
def display_info(employee):
    print("\nEmployee Information")
    for key, value in employee.items():
        print(f"{key.capitalize()}:{value}")
        

#Calling functions
employee = emp_dictionary()
display_info(employee)