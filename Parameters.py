# Author: Tithy
# Date: 2026-07-13
# Description: Functions with parameters.
# parameters recieve values and Arguments are the actual values.

def greet_user(name): #Name - Parameter
    print(f"Hi {name}! Welcome to the Python program.")
    
def user_info(name, age):
    print(f"I'm {name} and I'm {age} years old.")

#Functions calling
greet_user("Jane") #Jane and John - Arguments
greet_user("John")

user_info("Jane", 25)
user_info("John", 30)