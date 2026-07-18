# Author: Tithy
# Date: 2026-07-18
# Description: Generating random values using Python.

import random

#Generating random numbers
for i in range(3):
    print("Random numbers: ",random.random())
    
#Generating random integers
for i in range(3):
    print("Random integers: ", random.randint(1, 10))
    
#Randomly selecting team member
members = ['John', 'Tithy', 'Michael', 'Sarah', 'Jane', 'Jake']
leader = random.choice(members)
print("Leader: ", leader)