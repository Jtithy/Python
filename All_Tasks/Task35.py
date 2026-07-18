# Author: Tithy
# Date: 2026-07-18
# Description: Create a roll&dice game that shows different values "{a, b}" every time.

import random

for i in range(1):
    dice_roll_1 = random.randint(1, 6)
    for i in range(1):
        dice_roll_2 = random.randint(1, 6)
        print("Dice roll:  {", dice_roll_1, ",", dice_roll_2, "}")

    

