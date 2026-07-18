#Author: Tithy
#Date: 2026-07-12
#Description: Implement a program to calculate the total cost of a shopping cart.

shopping_cart = [20, 345, 60.50, 3000]
total_cost = 0
for item in shopping_cart:
    total_cost += item
print("Total cost of all items is: " +str(total_cost))