while True:
	try:
		user_choice_n = int(input("Please enter the""number in your equation: "))

		while True:
		
			if (3 == user_choice_n):

				break

			else:
				user_choice_n = int(input("Please only use the provided number and do not use each provided number more than once or use. Enter the""number in your equation:"))
			
		break

	except ValueError:
		print("Yeah,no. That's not an integer.")

	
#	except ValueError:
#		print("Yeah,no. That's not an integer.")