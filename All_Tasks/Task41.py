#Author: Tithy
#Date: 2026-07-21
#Description: Simulate flipping a coin 100 times and count heads/tails.



import random


heads = 0
tails = 0

for _ in range(100):
    if random.randint(0, 1) == 0:
        heads += 1
    else:
        tails += 1

print(f"Heads: {heads}")
print(f"Tails: {tails}")