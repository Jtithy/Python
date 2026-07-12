#Author: Tithy
#Date: 2026-07-12
#Description: Implementing a car game where start to start car, stop to stop car and quit to terminate the game.


command = ""
while command.lower() != "quit" and command.upper() != "QUIT":
    command = input("Enter command (start/stop/quit): ")
    if command.upper() == "START" or command.lower() == "start":
        print("Car started...!")
    elif command.upper() == "STOP" or command.lower() == "stop":
        print("Car stopped...!")
    elif command.upper() == "QUIT" or command.lower() == "quit":
        break
    else:
        print("Sorry, enter a valid command.")

print("Game terminated..!")
