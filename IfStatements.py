#Author: Tithy
#Date: 2026-07-10
#Description: Implementation os conditional statements.

is_hot = input("It's a hot day? (y/n): ")

if is_hot == "y":
    print("It's a hot day")
    print("Don't forget to drink water.")
elif is_hot == "n":
    print("It's a cold day.")
else:
    print("Please enter 'y' or 'n'.")