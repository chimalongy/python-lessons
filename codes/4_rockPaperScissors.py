import sys
import random
from enum import Enum
# DEMOSTRATION IF USER INPUTS

# value = input('Please enter a value:\n')
# print(value)


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()
# print("******")
playerchoice = input(
    "Enter ...'\n1. for Rock,\n2. for Paper, or \n3. for Scissors:\n\n")

player = int(playerchoice)
if player < 1 or player > 3:
    sys.exit("⚠ You must enter 1,2 or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")

if player == 1 and computer == 3:
    print('🎉 You win!')
elif player == 2 and computer == 1:
    print('🎉 You win!')
elif player == 3 and computer == 2:
    print('🎉 You win!')
elif player == computer:
    print('➰Tie game!')
else:
    print("💔 Python won")
print("*****")
