def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num

