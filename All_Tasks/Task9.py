#Author: Tithy
#Date: 2026-07-11
#Description: While loop to implement a guessing game that guess a number and there's will be 3 chances to guess.

secret_number = 7
print("Welcome to the guessing game!")
i = 1
while i <= 3:
    guess = int(input("Guess the secret integer number between 1 to 10: "))

    if guess == secret_number:
        print("You win!")
        break
    else:
        print("You lost! Try again.")
    i +=1
print("Thanks for playing!")