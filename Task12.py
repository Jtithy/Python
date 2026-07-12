#Author: Tithy
#Date: 2026-07-12
#Description: Implementing pattern using nested loop.

numbers = [5, 2, 5, 2, 2]

for count in numbers:
    # print('*' * count)
    output = ''
    for i in range(count):
        output += '*'
    print(output)