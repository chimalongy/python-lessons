import sys
import random
from enum import Enum
# DEMOSTRATION IF USER INPUTS

# value = input('Please enter a value:\n')
# print(value)


def rockPaperScissors():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input(
        "Enter ...'\n1. for Rock,\n2. for Paper, or \n3. for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("⚠ You must enter 1, 2 or 3.")
        return rockPaperScissors()

    player = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("You chose " + str(RPS(player)).replace("RPS.", "") + ".\n")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    if player == 1 and computer == 3:
        print('🎉 You win!')
    elif player == 2 and computer == 1:
        print('🎉 You win!')
    elif player == 3 and computer == 2:
        print('🎉 You win!')
    elif player == computer:
        print('➰Tie game!')
    else:
        print("🐍 Python won")
    print("*****")

    print("\n😜 Play Again?")

    while True:
        playagain = input("\nPlay again?\nY for Yes or\nQ to Quite\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return rockPaperScissors()
    else:
        print("\n 👍👍Thank you for playing \n")
        sys.exit("👋Bye")


rockPaperScissors()
