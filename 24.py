#The 24 Game
#sep17-sep23, 2018
#by Eric Li
#sources: Jerry Wang, Revant Kantamneni, Ms. Healey
#On my honor.

#This is the 24 game. The 24 Game is an arithmetical game in which the objective is to find a way to manipulate four numbers so that the end result is 24.
#In this game, the user will be provided with four different randomly generated integers ranging from 1 to 13.
#The allowed operatoions are addition, subtraction, multiplication, division, and exponentiation.
#In this game the user is only allowed to use each provided number once, and must use all four provided numbers.
#The user will be asked if he/she wants to start over when he/she 1)cannot find a solution 2)does not get the answer 24 3)wins the game
#The user may not use parenthesis in his/her equations.

import random as r
import sys
import time
import math

#a list of all the allowed symbols
allowed_symbols = [ '+', '-', '/', '**', '^', '*']
#storing the numbers the user has already entered
userOrder = []
#the default username
username = "Player One"
#the default result value
result = None
#the default list named "numbers"
numbers = []

def start():
	#allows me to store the user's name in the program
	global username

	#asking the user if he/she wants to store his/her name in the system
	print ("Hello "+username+"!")
	time.sleep(1)
	print("Would you prefer to \n   1)continue playing this game anonymously\n   2)register your name in the system")
	username_option = input()

	#response to the user's choice & error checking
	while True:
		#if the user prefers to stay anonymous, username stays at its default value
		if username_option == "1":
			time.sleep(0.5)
			print("\nWelcome to the 24 Game, "+username+".")
			break

		#if the user chooses to enter his/her name, username becomes the input value
		elif username_option == "2":
			time.sleep(0.5)
			username = input("Please enter your name: ")
			time.sleep(0.5)
			print("\nHello "+username+"! Welcome to the 24 Game.")
			break

		#error checking
		else:
			print("Please enter 1 or 2 to indicate your decision")
			time.sleep(0.5)
			print("\nWould you prefer to \n   1)continue playing this game anonymously or\n   2)register your name in the system? ")
			username_option = input()

	#printing out instructions
	time.sleep(1.5)
	print("Please read through the instructions before the game starts.")
	time.sleep(2)
	print("\n   The 24 Game is an arithmetical game in which the objective is to find\n   a way to manipulate four numbers so that the end result is 24.\n\n   In this game, you will be provided with four different randomly generated\n   integers ranging from 1 to 13.\n\n   The allowed operatoions are addition(+), subtraction(-), multiplication(*),\n   division(/), and exponentiation(** or ^).\n\n   In this game you are only allowed to use each provided number once.\n\n   You may not use parenthesis in your equations.")	
	time.sleep(15)
	print("\n"*2)
	#starting the game
	game()





def game():
	#allowing the list "numbers" to change each time the function "game" is called
	global numbers, userOrder

	#reset the numbers the user has entered everytime the function is called
	userOrder = []


	#this list makes sure that all four numbers are different
	numbers = r.sample([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],4)

	#providing the user the provided numbers
	print("Your numbers have been generated:")
	print(numbers)
	time.sleep(1)
	#asking the user if he/she has a solution in his/her mind
	print("Do you see a way to get to the answer 24?\n   1)Enter 1 for Yes\n   2)Press ENTER for No (new numbers will be generated)")
	solution = input()

	#response to the user's choice & error checking
	while True:
			# if the user has a solution in mind, the program asks him/her to enter his/her solution
			if solution == "1":
				print("Please enter your solution below:\n")
				getNum("first")
				getOperator("first")
				getNum("second")
				calculation("first",userOrder[0],userOrder[1])
				getOperator("second")
				getNum("third")
				calculation("second",result,userOrder[2])
				getOperator("last")
				getNum("last")
				calculation("last",result,userOrder[3])

				#the program checks to see if the answer is correct
				#if the answer is correct, the program congradulates the user, and asks if the user wants to play again
				if result == 24:
					print("\nCongratulations, "+username+"! You won!\n")
					start_over()

				#if the answer is not correct, the program states that there is an error, and asks if the user wants to play again
				else: 
					print("Oops, it seems that you have made a mistake in your calculation")
					start_over()

			# if the user does not gave a solution in mind, the program asks him/her if he/she wants to start over
			elif solution == "":
				game()

			#error checking
			else:
				print("Please enter 1 or press ENTER to indicate your decision")
				print("Do you see a way to get to the answer 24?\n   1)Enter 1 for Yes\n   2)Press ENTER for No (new numbers will be generated)")
				solution = input()




def start_over():
	#asking the user if he/she wants to start over
	print("Do you want to start again?\n   1)Yes\n   2)No")
	start_over = input()

	#response to the user's choice & error checking
	while True:
		#function game is called  if the user chooses to play again
		if start_over == "1":
			game()
			break
		elif start_over =="2":
			sys.exit()
			break
		else:
			print("Please enter 1 or 2 to indicate your decision")
			time.sleep(0.5)
			print("Do you want to start again?\n   1)Yes\n   2)No")
			start_over = input()


def getNum(num_ordinal):
	global userOrder, count

	#the functon checks to see if the number entered is an integer and if the number is one of the provided numbers and is not the same as any of the previously entered numebrs
	while True:
		try:
			print("Please enter the",num_ordinal,"number in your equation: ")
			user_choice = int(input())

			#checking to make sure that the value the user enters is one of the provided numbers and is not the same as any of the previously entered numebrs
			while True:
				if ((user_choice in numbers) and (user_choice not in userOrder)):
					userOrder.append(user_choice)
					break

				elif ((user_choice in numbers) and (user_choice in userOrder)):
					print("Do not use each provided number more than once or use.")
					print("Enter the",num_ordinal,"number in your equation:")	
					user_choice = int(input())

				else:
					print("Please only use the provided number.")
					print("Enter the",num_ordinal,"number in your equation:")
					user_choice = int(input())
				
			break

		#checking for ValueError
		except ValueError:
			print("Please enter an integer.")


def getOperator(operator_ordinal):
	global operator

	#asking for an operator input
	print("Please enter the",operator_ordinal,"operator in your equation.")
	#printing specific instructions regarding the allowed symbols if it asks the user to enter an operator for the first time
	if operator_ordinal == "first":
		print("Your may only choose from one of the following operators: \n+, -, *, /, ** or ^")
	
	operator = input()

	#checking to make sure that the operator entered is one of the allowed operators
	while True:
		if operator in allowed_symbols:
			break

		else:
			print("Your may only choose from one of the following operators: \n+, -, *, /, ** or ^")
			operator = input()

def calculation(operator_ordinal, constant1, constant2):
	global result

	#the function calculates the result of each step based on the numbers and operators provided
	if operator == "+":
		result = int(constant1) + int(constant2)
	
	elif operator == "-":
		result = int(constant1) - int(constant2)

	elif operator == "/":
		result = int(constant1) / int(constant2)

	elif operator == "*":
		result = int(constant1) * int(constant2)

	elif operator == "**" or operator == "^":
		result = int(constant1) ** int(constant2)

	print("Your",operator_ordinal,"operation evaluates to:",result)


start()



