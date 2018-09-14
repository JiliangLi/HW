#sep 9 2018
#first homework assignment conversation
#a conversation about one's favorate course and name at choate 
#in this conversation only two answers (CS550 and computer science) are considered "correct"
#jerry  and revant as resources

print("Hello, how are you doing today")

def question():
	answer1 = input("What's your favorite course at Choate?")
	if answer1 == "CS550" or answer1 == "Computer science":
		print("Welcome to CS550")
		username = input("What is your name?")
		print("It's nice to meet you, "+username)

	else:
		print("Wrong answer!!!")
		question()

question()

