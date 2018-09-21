import sys
import time
import math
import random as r

number1 = None
number2 = None
number3 = None
number4 = None
username = "Player One"
result = None
allowed_symbols = None

def start():
	global username
	global allowed_symbols
	global number1, number2, number3, number4
	global usernumber1, usernumber2, usernumber3, usernumber4
	global result
	global usersymbol1, usersymbol2, usersymbol3

	print ("Hello "+username+"!")
	time.sleep(1)
	username_option = input("Would you prefer to 1)continue playing this game anonymously or 2) register your name in the system?")

	while True:
		if username_option == "1":
			print("Welcome to the 24 Game, "+username+".")
			break

		elif username_option == "2":
			username = input("Please enter your name: ")
			print("Hello "+username+"! Welcome to the 24 Game.")
			break

		else:
			print("Please enter 1 or 2 to indicate your decision")
			time.sleep(1)
			username_option = input("Would you prefer to 1)continue playing this game anonymously or 2) register your name in the system?")

	rules()
	game()

def rules():
	print("In this game, you will be provided with...")
	#time.sleep(1)

def game():
	global allowed_symbols
	global number1, number2, number3, number4
	global usernumber1, usernumber2, usernumber3, usernumber4
	global result
	global usersymbol1, usersymbol2, usersymbol3
	allowed_symbols = [ '+', '-', '/', '**', '^', '*']

	number1 = str(r.randrange(1,14,1))
	number2 = str(r.randrange(1,14,1))
	number3 = str(r.randrange(1,14,1))
	number4 = str(r.randrange(1,14,1))

	print(number1)
	print(number2)
	print(number3)
	print(number4)

	generated_list = [number1,number2, number3, number4]

	usernumber1 = input("Please enter the first number in your equation: ")
	while True:
		if usernumber1 == number1:
			usersymbol1_usernumber2()
			#usersymbo(number1)
			while True:
				if usernumber2 == number2:
					usersymbol2_usernumber3()

					while True:		
						if usernumber3 == number3:
							usersymbol3_usernumber4()
							while True:
								if usernumber4 == number4:
									operation(result, usersymbol3, usernumber4)
									break
								else:
									usernumber4 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the last number in your equation: ")
							break

						if usernumber3 == number4:
							usersymbol3_usernumber4()
							while True:
								if usernumber4 == number3:
									operation(result, usersymbol3, usernumber4)
									break
								else:
									usernumber4 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the last number in your equation: ")
							break
						
						else:
							usernumber3 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the third number in your equation: ")
					break

				if usernumber2 == number3:
					usersymbol2_usernumber3()
					
					while True:
						if usernumber3 == number4:
							usersymbol3_usernumber4()
							while True:
								if usernumber4 == number2:
									operation(result, usersymbol3, usernumber4)
									break
								else:
									usernumber4 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the last number in your equation: ")
							break

						if usernumber3 == number2:
							usersymbol3_usernumber4()
							while True:
								if usernumber4 == number4:
									operation(result, usersymbol3, usernumber4)
									break
								else:
									usernumber4 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the last number in your equation: ")
							break

						else:
							usernumber3 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the third number in your equation: ")

					break

				if usernumber2 == number4:
					usersymbol2_usernumber3()
					while True:
						if usernumber3 == number2:
							usersymbol3_usernumber4()
							while True:
								if usernumber4 == number3:
									operation(result, usersymbol3, usernumber4)
									break
								else:
									usernumber4 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the last number in your equation: ")
							break

						if usernumber3 == number3:
							usersymbol3_usernumber4()
							while True:
								if usernumber4 == number2:
									operation(result, usersymbol3, usernumber4)
									break
								else:
									usernumber4 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the last number in your equation: ")
							break
						else:
							usernumber3 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the third number in your equation: ")
					break
				else:
					usernumber2 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the second number in your equation: ")

			break


		if usernumber1 == number2:
			pass
			break

		if usernumber1 == number3:
			pass
			break


		if usernumber1 == number4:
			pass
			break

		else:
			usernumber1 = input("Please only use the provided number and do not use each provided number more than once or use. Enter the last number in your equation: ")


def operation(constant1, symbol, constant2):
	global allowed_symbols
	global number1, number2, number3, number4
	global usernumber1, usernumber2, usernumber3, usernumber4
	global result
	global usersymbol1, usersymbol2, usersymbol3	

	if symbol == "+":
		result = int(constant1) + int(constant2)
	
	elif symbol == "-":
		result = int(constant1) - int(constant2)

	elif symbol == "/":
		result = int(constant1) / int(constant2)

	elif symbol == "*":
		result = int(constant1) * int(constant2)

	elif symbol == "**" or symbol == "^":
		result = int(constant1) ** int(constant2)

	print(f'DEBUG: symbol is {symbol}, result is {result}, constant1 is {constant1}, constant2 is {constant2}')


	print("Your operation evaluates to:",result)

def operator_check(value):
	global allowed_symbols
	global number1, number2, number3, number4
	global usernumber1, usernumber2, usernumber3, usernumber4
	global result
	global usersymbol1, usersymbol2, usersymbol3

	while True:
		if value in allowed_symbols:
			break

		else:
			value = input("Your may only choose from one of the following operators: \n+, -, *, /, ** or ^\n")

	return value


def usersymbol1_usernumber2():
	global allowed_symbols
	global number1, number2, number3, number4
	global usernumber1, usernumber2, usernumber3, usernumber4
	global result
	global usersymbol1, usersymbol2, usersymbol3

	usersymbol1 = input("Please enter the first operator in your equation. \nYour may only choose from one of the following operators: \n+, -, *, /, ** or ^\n")
	usersymbol1 = operator_check(usersymbol1)
	usernumber2 = input("Please enter the second number in your equation: ")

def usersymbol2_usernumber3():
	global allowed_symbols
	global number1, number2, number3, number4
	global usernumber1, usernumber2, usernumber3, usernumber4
	global result
	global usersymbol1, usersymbol2, usersymbol3

	operation(usernumber1, usersymbol1, usernumber2)
	usersymbol2 = input("Please enter the second operator in your equation. \nYour may only choose from one of the following operators: \n+, -, *, /, ** or ^\n")
	usersymbol2 = operator_check(usersymbol2)
	usernumber3 = input("Please enter the third number in your equation: ")

def usersymbol3_usernumber4():
	global allowed_symbols
	global number1, number2, number3, number4
	global usernumber1, usernumber2, usernumber3, usernumber4
	global result
	global usersymbol1, usersymbol2, usersymbol3

	operation(result, usersymbol2, usernumber3)
	usersymbol3 = input("Please enter the third operator in your equation. \nYour may only choose from one of the following operators: \n+, -, *, /, ** or ^\n")
	usersymbok3 = operator_check(usersymbol3)
	usernumber4 = input("Please enter the last number in your equation: ")


start()











