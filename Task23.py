# Author: Tithy
# Date: 2026-07-16
# Description: Rotate a list to the left by one position.

def rotate_left(list):
    if not list:
        return None
    first_element = list[0]
    for i in range(len(list) - 1):
        list[i] = list[i+1]
        list[-1] = first_element
    return list

list = input("Enter elements separated by space: ").split()
rotate_list = rotate_left(list)
print("Left rotate of list: ", rotate_list)