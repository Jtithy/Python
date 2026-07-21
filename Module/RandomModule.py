#Author: Tithy
#Date: 2026-07-21
#Description: Random Module demonstration.

import random

name_list = input("Enter names separated by space: ").split()
random_name = random.choice(name_list)
print(f"Randomly selected name: {random_name}")