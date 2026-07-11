#Author: Tithy
#Date: 2026-07-11
#Description: Implementing comparison operators in Python.

temperature = float(input("Enter today's temperature in celsius: "))

if temperature < 5:
    print("It's a very cold day.")
elif temperature > 5 and temperature < 15:
    print("It's a cold day.")
elif temperature > 15 and temperature < 27:
    if temperature == 25:
        print("It's a perfect day.")
    else:
        print("It's a warm day.")
elif temperature > 27 and temperature < 40:
    print("It's a hot day.")
elif temperature > 40:
    print("It's a very hot day.")