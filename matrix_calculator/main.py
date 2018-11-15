# matrix calculator
# nov 2 - nov 15, 2018
# by Eric Li
# source: Ms. Healey, Jerry Wang
# on my honor

# this is a program that generates does two types of matrix calculations:
#	1) reduced row echelon form (rref) calculation
#	2) inverse matrix calculation 

# terms explained:
#	1) the size of a matrix with m rows and n columns is said to be of size m*n
#	2) identity matrix (I): the diagnal matrix whose nonezero entries are all 1
#	3) the rref:
#		1. all nonzero rows (rows with at least one nonzero element) are above any rows of all zeroes (all zero rows, if any, belong at the bottom of the matrix)
#		2. the leading coefficient (the first nonzero number from the left, also called the pivot) of a nonzero row is always strictly to the right of the leading coefficient of the row above it.
#		3. the leading entry in each nonzero row is a 1 (called a leading 1).
#		4. each column containing a leading 1 has zeros everywhere else.
#	4) the inverse:
#		the inverse of matrix A, denoted A**-1 is the matrix such that A*(A**-1/) = I = (A**-1)*A
#	
# inverse calcualtion explained:
#	one of the many ways to get the inverse of the invertible matrix A is that:
#		augment I to to A
#		do all row operations that lead A to its rref form (in this case because A is invertible rref(A)=I) to the augmented I as well
#		when A is reduced to its rref form, the agumented matrix I becomes A's inverse

# the program askes the user to generate a matrix based on:
#	1) the size of the matrix
#	2) each entry in the matrixautomatically
# the program askes the user to choose between rref and inverse calculation
# based on the user's choice, the program calculates the corresponding matrix
# the program prints out the inverse as it is, and it prints out the rref form of the matrix in a nice grid

# link file
from theMatrix import Matrix

# the function creates a grid for the rref matrix
def print_matrix(mat):
	c=-1
	for entry in mat[0]:
		c+=len(str(entry))+1

	print(' '+'-'*c+' ')			# add horizontal lines at the top
	for row in mat:
		print('|',end='')			# add vertical lines on the left
		for entry in row:
			print(entry,end='')
			print('|',end='')		# add vertical lines in the middle and on the right
		print()
		print(' '+'-'*c+' ')		# add horizontal lines in the middle and on the bottom


# the function askes for the user's input and has error checking abilities
def entry():
	global the_matrix
	while True:
		try:
			print("Please enter the dimension of the matrix: \n(for instance, if the matrix is a 2 by 5 matrix, enter 2*5)")
			dimension_raw = input()
			dimension = dimension_raw.split('*')
			if len(dimension) == 2:				# check to see if it is a 2D matrix
				dimension[0] = int(dimension[0])	# number of rows
				dimension[1] = int(dimension[1])	# number of columns
				break
			else:
				print("please enter a valid dimension connected by '*'")
			

		except ValueError:
			print("Please enter a valid dimension connected by '*'")

	rows= []
	matrix_list = [[0 for i in range(dimension[1])]for i in range(dimension[0])]			# generate a list version of the matrix first
	for i in range(dimension[0]):			# for each row in the matrix
			position = "row "+str(i+1)
			rows.append(position)			# store the position for it to be printed out
			print("Please enter the values of the entries in "  + position+ " (separated by space): ")
			while True:
				try:
					while True:
						rowi = input()
						rowi = rowi.split()			# allows for the program to take in multiple entries at a time
						if len(rowi) == dimension[1]:	#check to see if the number of entries correspond with the size of the matrix
							matrix_list[i] = rowi
							break
						else:
							print("Please create a matrix corresponding to column number " + str(dimension[1])+".")

					for j in range(dimension[1]):
						matrix_list[i][j] = float(matrix_list[i][j])			# turn all strings into floats for further calculation
					break

				except ValueError:			#check to see if all entries are valid
					print("Please enter entries that are real numbers.")

	the_matrix = Matrix(matrix_list,dimension[0],dimension[1])			# generate the matrix in the class defined in the separate file


# the function asks the user for the type fo calculation and prints out the result
def output():
	print("Would you like to find:\n    1)The rref\n    2)The inverse")				# asks the user for the type of calculation
	while True:
		user_choice = input()
		if user_choice == "1" or user_choice == "2":
			print("The result is: ")
			if user_choice == "1":
				print_matrix(the_matrix.calc("rref"))			# print the rref form with the grid
			if user_choice == "2":
				# we are not printing the inverse in a grid because each entry in the inverse typically has numerous digits
				# so it doesn't look good with the grid
				print(the_matrix.calc("inverse"))			
			break
		else:			# error checking
			print("Please enter 1 or 2 to indicate you choice.")

#run the functions
entry()
output()


