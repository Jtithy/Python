# Author: Tithy
# Date: 2026-07-16
# Description: Print all multiplication tables from 1 to 10.

def print_multiplication_table():
    for i in range(1, 11):
        print(f"Multiplication table for {i}: ")
        for j in range(1, 11):
            print(f"{i} X {j} = {i*j}")
    

print_multiplication_table()