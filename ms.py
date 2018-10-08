# oct 1 - oct 6, 2018
# Eric Li

# the minesweeper

# Th user provide the width (W) and the height (H) for the program
# as well as the number of  bombs on the board.  
# The bombs (B) will be randomly placed,  
# and then the program determines how many bombs surround each space. 
# the user chooses a space to either clear or flag.
# if the user chooses a flag, then the space will be marked flag. 
# the user has the chance to unflag each flaged space.
# if the user chooses to reveal, then the number underneath will be revealed. 
# if the space revealed is a Dzzerodz space, then all touching zero spaces will be revealed, as well as the first non-zero contiguous space.
# if the space revealed is a  bomb,  then the user loses the game.
# when  all  safe spaces are revealed, the user wins the game. 
# after each game the user is asked whether if he/she wants to start over or quit

import sys
import random

if len(sys.argv) == 4:			#if the command line is correctly entered, set up the following values
	row = sys.argv[1]			#number of rows
	column = sys.argv[2]			#number of columns
	b = sys.argv[3]			#number of bombs
	count = 0
	row_count = 1
	x_y = []
	field_display = [["·"]*(int(column)) for x in range(int(row))]			#the field that is displayed to the user
	field = [[0]*int(column) for x in range(int(row))]			#the actual field that is not revealed until the end of the game
	check_x_y = []
	doublecheck_x_y = []
	bomb_count = 0
	win_lose = 1
	number_count = 0




def field_setup():			#function that sets up the field
	global row, column, b, count, row_count, x_y, field, user_y, user_x

	#enter all coordinate in the matrix into a new list
	for i in range(int(row)):
		for j in range(int(column)):
			x_y.append([i,j])	
	random.shuffle(x_y)			#randomize the list so that the coordinate will be randomly chosen

	x_y.remove([user_y, user_x]) #remove the user's first choice from the list so that a bomb is not placed at the user's first choice

	#randomly place the amount of bombs indicated by the user using the randomized list
	while count < int(b): 
		x = x_y[0][1]
		y = x_y[0][0]
		field[y][x] = "*"
		x_y.pop(0)			#remove the used coordinate from the list so that no more than one bomb is placed at each space
		count += 1

	#enlarge the size of the matrix so that no error may occur when adding numbers to the eight spaces surrounding each bomb
	for j in range(int(row)):
		field[j] = [0] + field[j] + [0]
	field = [[0]*(int(column)+2)] + field + [[0]*(int(column)+2)]

	#for each bomb detected the program adds 1 to the 8 surrounding spaces
	while row_count < (int(row)+1):
		for k in range(1, int(column)+1):
			if field[int(row_count)][k] == "*":
				for i in range(-1,2):
					for j in range(-1,2):
						if field[int(row_count)+i][k+j] != "*":
							field[int(row_count)+i][k+j] += 1
		row_count += 1

	#reduce the matrix to its normal size
	for j in range(int(row)+2):
		field[j].pop(0)
		field[j].pop((int(column)))
	field.pop(0)
	field.pop(int(row))




def print_field_display():			#function that prints the field shown to the user
	global field_display, row

	for i in range(int(row)):
		print(*field_display[i])

def print_field():			#function that prints the actual field
	global field, row

	for i in range(int(row)):
		print(*field[i])

def completion_check():			#function that helps check if all bombs are left blank or flagged/function that helps check if the game if over
	global row, column, field_display, bomb_count

	for i in range(int(row)):
		for j in range(int(column)):
			if field_display[i][j] == "·" or field_display[i][j] == "F":
				bomb_count += 1




def clear():			#the function that is run when the user decides to clear an unrevealed space
	global field, field_display, check_x, check_y, check_x_y, doublecheck_x_y, bomb_count, win_lose

	if field[user_y][user_x] == "*":			#scenario when the user clears a bomb
		field_display[user_y][user_x] = field[user_y][user_x]
		print_field_display()
		print("\nYou Lost")			#showing that the user loses
		bomb_count = int(b)			#indicating that the user has already completed the game
		win_lose -= 1				#indicating that the user has already lost the game

	elif field[user_y][user_x] != 0 and field[user_y][user_x] != "*":			#scenario when the user clears a non-zero space
		field_display[user_y][user_x] = field[user_y][user_x]			#only the non-zero space is revealed
		print_field_display()

	else:			#scenario when the user clears a zero space: all touching zero spaces will be revealed, as well as the first non-zero contiguous spaces
		check_x_y.append([user_y,user_x])			#the coordinate of the zero space is added to a new list that includes all the touching zero spaces discovered and have not been checked yet
		doublecheck_x_y.append([user_y,user_x])			#the coordinate of the zero space is added to a new list that includes all the touching zero spaces that are discovered

		while len(check_x_y) != 0:			#when there's still zero spaces that remains unchecked
			check_y = check_x_y[0][0]
			check_x = check_x_y[0][1]

			field_display[check_y][check_x] = field[check_y][check_x]			#reveal the zero space

			#reveal all the non-zero contiguous spaces
			for i in range(-1,2):
				for j in range(-1,2):
					if check_y + i >= 0 and check_y + i <= (int(row) -1) and check_x + j >= 0 and check_x + j <= (int(column) -1):			#making sure that each coordinate does not exceed the boundaries
							if [i,j] != [0,0]:			#if a contiguous space is not zero, reveal the space
								field_display[check_y+i][check_x+j] = field[check_y+i][check_x+j]

								if field[check_y+i][check_x+j] == 0 and [check_y+i, check_x+j] not in doublecheck_x_y:			#if the contiguous space is zero and is not already on the waitlist to be checked 
									check_x_y.append([check_y+i, check_x+j]) 			#add it to list check_x_y for it to be checked
									doublecheck_x_y.append([check_y+i, check_x+j])			#indicate that this coordinate is alreay waiting to be checked
			check_x_y.pop(0)			#once the coorindate is checked, remove it from the list so that it doesn't get checked the second time

		print_field_display()			#print the field




def minesweeper():			#the main game function
	global field, field_display, bomb_count, check_x, check_y, user_x, user_y, win_lose, number_count

	#this function is separated into two sections becasue the bombs needs to be placed/the field needs to be generated after the user enters his/her first choice so that the user does not clear a bomb/lose the game at his/her first entry

	#section 1: user's first choice
	print("Your game board is generated：") 
	print_field_display()				#generate the displayed game board

	print("To start off, please choose a coordinate to clear:\n(For example, if you want to choose [1,1], enter '1 1')")
	
	#asking the user to choose a space while checking through all potential value errors
	while True:
		try:
			userchoice = input("")
			userchoice_split = userchoice.split()			#turning the user's input into a list, which allows the program to use each individual number more easily
			if len(userchoice_split) == 2:			#if the user puts in a valid coordinate
				user_y = int(userchoice_split[0]) - 1
				user_x = int(userchoice_split[1]) -1

				if 0 < user_y+1 <= int(row) and 0 < user_x+1 <= int(column):			#set up the field and reveal the appropriate spaces if the user puts in a valid coordinate
					field_setup()
					clear()
					
					break

				else:			#if the user does not put in a valid coordinate
					print("Please enter the correct coordinate within the matrix.")
			else:			#if the user does not put in a coordinate
				print("Please enter the correct coordinate.")

		except ValueError:			#if the coordinate entered is not valid
			print("Please enter a number.")

	
	#section 2: user's following choices
	completion_check()			#check to see if the user has revealed all the safe spaces already/check to see if the game is over

	while bomb_count != int(b):			#while all bombs are not either left blank or flagged/while the game is still not over
		print("Please choose another space:")
		
		if number_count == 0:		#print the following if this is the first time the function is run
			print("Note: Enter just the coordinate if you want to clear that space.\n      Enter f after the coordinate if you intend to flag/unflag the chosen space.")

		while True:
			#asking the user to choose a space while checking through all potential value errors
			try:
				userchoice = input("")
				userchoice_split = userchoice.split()
				user_y = int(userchoice_split[0]) - 1			#turning the user's input into a list, which allows the program to use each individual number more easily
				user_x = int(userchoice_split[1]) -1
				if (len(userchoice_split) == 3 or len(userchoice_split) == 2):			#if the coordinate entered is valid
					if 0 < user_y+1 <= int(row) and 0 < user_x+1 <= int(column):			#if the coordinate entered is within the matrix
						if len(userchoice_split) == 3:			#if there's three entries
							if userchoice_split[2] == "f":			#unflag the space if the user chooses a flaged space
								if field_display[user_y][user_x] == "F":
									field_display[user_y][user_x] = "·"
									print_field_display()
								elif field_display[user_y][user_x] == "·":			#flag the space if the user chooses a unflagged space
									field_display[user_y][user_x] = "F"
									print_field_display()
								else:			#making sure that the user doesn't flag a revealed safe space
									print("You may not select a revealed space.")
							else: 			#making sure that the user, instead of flagging the space, doesn't indend to enter an invalid coordinate
								print("Please only use 2 values in your coordinate entry")
				

						elif len(userchoice_split) == 2:			#if the user decides to clear a space
							if field_display[user_y][user_x] == "·":			#if the space is unrevealed
								clear()				#reveal all appropriate spaces/results

							else:			#stating that the user cannot reveal a revealed space
								print("You may not select a revealed space.")
						
					else:			#if the coordinate entered is not within the matrix
						print("Please enter the correct coordinate within the matrix.")

					break

				else:			#if the coordinate entered is not valid
					print("Please enter the correct coordinate")
			
			except ValueError:			#if the coordinate entered is not valid
				print("Please enter a number.")
	
		
		if bomb_count != int(b):			#if it is not indicated that the user has already completed the game
			bomb_count = 0			#zero out the bomb_count each time the function is run so that the complete_check function may determin if all bombs are left blank or flagged for each time the user reveals/flags/unflags a space

			completion_check()

		number_count += 1			#indicate the amount of times the function is run
				
	if win_lose == 1:			#if it is not indicated that the user has already lost the game
		print("\nCongratulations! You have cleared all the bombs!")

	#show the user what the actual looks like by the end of each game
	print("The field looks like:\n")
	print_field()


#check whether if the command line arguments are correctly & appropriately entered
if len(sys.argv) == 4:			
	if 0 < int(b) < (int(row)*int(column)):			#if the number of bombs is resonably entered
		minesweeper()

		while True:			#allowing for the user choose between restarting and quiting after each game
			try:
				restart = int(input("\nWould you like to 1)start a new game 2)quit "))

				if restart == 1:			#reset all values and then restart the game
					count = 0
					row_count = 1
					x_y = []
					field_display = [["·"]*(int(column)) for x in range(int(row))]
					field = [[0]*int(column) for x in range(int(row))]
					check_x_y = []
					doublecheck_x_y = []
					bomb_count = 0
					win_lose = 1
					number_count = 0

					minesweeper()

				elif restart == 2:
					sys.exit()

				else:
					print("Please enter 1 or 2 to indicate your choice.")

			except ValueError:
				print("Please enter a number.")

	else:
		print("The number of bombs may not be less than 1 or more than the (size of board - 1).\nPlease re-enter the game.")


else:
	print("The game expects 3 values (hight/width/number of bombs).\nPlease re-enter the game.")



