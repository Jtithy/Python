# Author: Tithy
# Date: 2026-07-12
# Description: Check whether a character is a vowel or consonant.  

alphabet = input("Enter a letter: ")

while not alphabet.isalpha() or len(alphabet) != 1:
    if not alphabet.isalpha():
        print("Enter valid input.")
    elif len(alphabet) != 1:
        print("Enter letter only.")
    alphabet = input("Enter a letter: ")
if alphabet == 'a' or alphabet == 'A':
    print("The letter is a vowel.")
elif alphabet == 'e' or alphabet == 'E':
    print("The letter is a vowel.")
elif alphabet == 'i' or alphabet == 'I':
    print("The letter is a vowel.")
elif alphabet == 'o' or alphabet == 'O':
    print("The letter is a vowel.")
elif alphabet == 'u' or alphabet == 'U':
    print("The letter is a vowel.")
else:
    print("The letter is a consonant.")

