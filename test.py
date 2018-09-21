import random as r

def game(name):

	number1 = str(r.randrange(1,14,1))
	number2 = str(r.randrange(1,14,1))
	number3 = str(r.randrange(1,14,1))
	number4 = str(r.randrange(1,14,1))

	print(number1)
	print(number2)
	print(number3)
	print(number4)


	usernumber1 = input("Please enter the first number in your solution: ")

	if usernumber1 == number1 or usernumber1 == number2 or usernumber1 == number3 or usernumber1 == number4:
		print("Hello")

	else:
		print("Please enter one of the provided number")
		game("Payer one")

game("player one")