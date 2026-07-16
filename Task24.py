# Author: Tithy
# Date: 2026-07-16
# Description: Check if a word is a palindrome using a list.

def is_palindrome(word):
    if not word:
        return None
    word_list = list(word)
    reversed_list = word_list[::-1]
    return word_list == reversed_list

word = input("Enter a word: ")
result = is_palindrome(word)
print(f"The word '{word}' is a palindrome: {result}")
