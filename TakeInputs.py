#Author: Tithy
#Date: 2026-07-10
#Description: Program to take inputs from users.

#Input form users
name = input("What's your name?")
code = input("What's the code?")

print('Name: ' +name+ ' and Code: ' +code)

#Input function with type casting
age = int(input("What's your age?"))
print('Age is: ' +str(age))

#Input as separate function
def take_input():
    name = input("What's your name?")
    code = input("What's the code?")
    print('Name: ' +name+ ' and Code: ' +code)

#Function call
take_input()
