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


odds = [i for i in range(1,37) if i % 2 != 0]
evens = [i for i in range(1,37) if i % 2 == 0]
reds = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
blacks = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
first_twelve = [i for i in range(1,13)]
second_twelve = [i for i in range(13,25)]
third_twelve = [i for i in range(25,37)]
bottom_strip = [(3 * n - 2) for n in range(1,13)]
middle_strip = [(3 * n - 1) for n in range(1,13)]
top_strip = [(3 * n) for n in range(1,13)]

def roulette(odd_even = None, red_black = None, twelve= None, strip = None, available_bank = 1):
	bank = available_bank
	turn = 1

	#You need a bet for each condition
	number_of_conditions = 0
	conditions_list = [odd_even, red_black, twelve, strip]
	for condition in conditions_list:	
		if condition != None:
			number_of_conditions += 1

	while bank > number_of_conditions:
		#print("£{}".format(bank))
		bank -= number_of_conditions
		spin = random.randint(0,36)
		#print("{}: Spinning...".format(turn))
		#print("{}!".format(spin))
		if odd_even:
			if spin in odd_even:
				bank += 2
		if red_black:
			if spin in red_black:
				bank += 2
		if twelve:
			if spin in twelve:
				bank += 3
		if strip:
			if spin in strip:
				bank += 3
		turn += 1
	return turn


# Function that plays roulette n times
# Prints Average, median, min and max game length

def stats(bank, iterations):
	list_of_turns = []
	min_turns = None
	max_turns = None
	for i in range(iterations):
		turns = roulette(twelve = first_twelve, available_bank = bank)
		list_of_turns.append(turns)

	print(list_of_turns)
	sorted_list_of_turns = sorted(list_of_turns)

	total = 0
	for n in list_of_turns:
		total += n
	average_turns = total / len(list_of_turns)

	median_turns = sorted_list_of_turns[len(list_of_turns)//2]
	min_turns = sorted_list_of_turns[0]
	max_turns = sorted_list_of_turns[-1]

	print("Average: {}".format(average_turns))
	print("Median: {}".format(median_turns))
	print("Max: {}".format(max_turns))
	print("Min: {}".format(min_turns))


#Call your game of chance functions here
stats(10, 100)
