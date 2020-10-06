# Codecademy Games of Chance

import random
import time

money = 100

#Write your game of chance functions here
def coin_flip():
	print("## Coin Toss ##")
	bet = input("How much would you like to bet: ")
	choice = input("Heads or tails? (h or t): ")
	if choice == "h":
		choice = "heads"
	else:
		choice = "tails"
	print ("You have chosen " + choice)
	print("Flipping coin...")
	time.sleep(1)
	result = random.randint(0,1)
	if result == 0:
		result = "heads"
	if result == 1:
		result = "tails"
	print(result.upper() + "!!")
	time.sleep(1)
	if choice == result:
		print("You win!")
		return bet
	else:
		print("Bad luck.")
		return bet * -1

def cho_han():
	print("## Cho-Han ##")
	bet = input("How much would you like to bet: ")
	choice = int(input("Select 0 for even, 1 for odd: "))
	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)
	print("Dice show {0} and {1}.".format(dice1, dice2))
	if ((dice1 + dice2) % 2) == choice :
		print("You win!!")
		return bet
	else:
		print ("Bad luck.")
		return bet * -1

def pick_a_card():
	print("~~ Pick a Card ~~")
	bet = input("How much would you like to bet: ")
	deck = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
	player1 = random.randint(0,12)
	player2 = random.randint(0,12)
	print ("Player 1 drew {0}".format(deck[player1]))
	print ("The dealer drew {0}".format(deck[player2]))
	if player1 > player2:
		print ("Player wins!")
		return bet
	elif player2 > player1:
		print ("Dealer wins!")
		return bet * -1
	else: print("Draw")

#def roulette():


#Call your game of chance functions here
