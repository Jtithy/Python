#Author: Tithy
#Date: 2026-07-11
#Description: Implementing a program that takes value and ask it's type and then convert it into different unit.

weight = float(input("Enter your weight: "))
unit = input("Enter the unit (pounds == P/p or kilograms == KG/kg): ")

if unit.upper() == "P" or unit.lower() == "p":
    weight_in_kg = weight * .4533
    print(f"You're {weight_in_kg:.2f} kilograms.")
    
elif unit.upper() == "KG" or unit.lower() == "kg":
    weight_in_pounds = weight / .4535
    print(f"You're {weight_in_pounds:.2f} pounds.")
    
else:
    print("Invalid unit!")