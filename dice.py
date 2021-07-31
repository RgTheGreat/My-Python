import random
dice1 = "\n-----\n| . |\n-----  1"
dice2 = "\n------\n| .. |\n------  2"
dice3 = "\n-------\n| ... |\n------  3"
dice4 = "\n--------\n| .... |\n------  4"
dice5 = "\n---------\n| ..... |\n------  5"
dice6 = "\n----------\n| ...... |\n------  6"

dices = [dice1, dice2, dice3, dice4, dice5, dice6]

random_dice1 = random.choice(dices) 

random_dice2 = random.choice(dices)

player1 = input("Player 1: ")

player2 = input("player 2: ")


print("player 1 got: " + random_dice1 + " and player 2 got: " + random_dice2)