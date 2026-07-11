#Author: Tithy
#Date: 2026-07-11
#Description: Price of a house is $1M. Is the buyer has good credit, they need to put down 10%, otherwise the need to put down 20%. Print the down payment.

house_price = 1000000
has_good_credit = input("Does the buyer has good credit? (t/f): ")
down_payment = 0

if has_good_credit == "t":
    down_payment = house_price * 0.1
    print(f"The down payment is: ${down_payment}")
elif has_good_credit == "f":
    down_payment = house_price * 0.2
    print(f"The down payment is: ${down_payment}")
else:
    print("Please enter 't' or 'f'")

