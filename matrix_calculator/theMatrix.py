# in order to use np.array()
import numpy as np

# create a class so that multiple matrices may be stored and same calucaltion can be performed
class Matrix:
	# constructor
	def __init__(self, main_matrix, number_rows, number_columns):
		self.matrix = np.array(main_matrix)			# turn the list version of the matrix in to an array
		self.matrix_reference = np.array(main_matrix).copy()		# create a reference so that the matrix may be reset
		
		# set up values for further calculations
		self.nonzero_rows = number_rows		# this value indicates the number of rows with at lease one nonzero entry
		self.total_row_swapped = 0			# this value indicates how many rows are swapped during the calculation
		self.number_columns = number_columns		# size of the matrix
		self.number_rows = number_rows				# size of the matrix
		self.identity = [[0 for i in range(number_rows)] for i in range(number_columns)]
		for i in range(number_rows):
			self.identity[i][i] = 1
		self.identity = np.array(self.identity)			# create an identity matrix for the potential inverse calculation

	# the method detects if there's a zero row in the matrix and moves it to the bottom of the matrix
	def check_zero_rows(self):
		zero_count = 0;
		count = 0
		while count < self.nonzero_rows:			# go through every row that are now labeled as nonzero
			if np.all(self.matrix[count] == 0) == True:			# if the row is turned into a zero row by the previous operation
				row_moved = self.matrix[count]
				self.matrix = np.delete(self.matrix, (count), axis = 0)			# removed the zero row
				zero_count += 1				# number of rows removed += 1
				self.nonzero_rows -= 1		# one fewer row labeled as nonzero
				self.total_row_swapped += 1			# now in total there's one more row swapped
			else:
				count += 1

		# add the same number of zero rows as the number of removed rows to the bottom of the array
		for i in range(zero_count):
			self.matrix = np.append(self.matrix, [row_moved], axis = 0)

	# the method returns the number of entries in each row following its pivot point
	def len_check(self, row):
		row_check = self.matrix[row].copy()			# make a copy so that the original matrix is not changed
		column_remaining = self.number_columns		# how many entries are left

		j = 0			# starting from the first entry in each row

		while j < column_remaining:
			if row_check[j] != 0:		# if this entry is nonzero	
				break	
			elif row_check[j] == 0:			# if this entry is zero	
				row_check = np.delete(row_check, j)		# removed the zero entry
				column_remaining -= 1			# how many entries are left; this makes sure that the while loop doesn't run beyond the length of the row that's left
		return len(row_check)			# return the length of the row that's left

	# the method, depending on the length of each row defined in len_check(), makes sure that all more lengthy rows are higher up than less lengthy rows
	# this helps makes sure that each column containing a leading nonzero entry has zeros everywhere else.
	def check_length_rows(self):
		rows_swapped = 0
		row_length = []
		for i in range(self.nonzero_rows):
			row_length.append(self.len_check(i))		# use a list to store all valeus for further cross comparisons

		i = 0
		# the program goes through all rows to make sure that the descending order is consistent throughout the matrix
		while i < (self.nonzero_rows-1):		
			if row_length[i+1] > row_length[i]:		# if the row higher up is shorter in length than the row beneath
				row_length[i], row_length[i+1] = row_length[i+1], row_length[i]			# store the swapped row lengths
				self.matrix[[i,i+1]] = self.matrix[[i+1,i]] 			# swap rows
				rows_swapped += 1
			i += 1

		# because each time when the function is run there's at most one row that is moved
		# no matter how many times that row is moved down, the total_row_swapped value only increases by one
		if rows_swapped != 0:			
			self.total_row_swapped += 1			

	# this method runs through both the rref calculation and the inverse calculation
	# no matter what the user_choice is, the method runs through the rref calculation first
	# because we first need to know, through the rref value, whether the matrix is invertible
	# for inverse calculation, once we know that the matrix is invertible, we run through the method again, this time indicating that we're doing inverse_calc
	# when the method is run for  inverse_calc it row operates the matrix, denoted A, along with the augmented identity matrix,
	# so that whatever row operation is done to A it is also done to the identity matrix
	# when A becomes I, the augmented I becomes A inverse
	def calc(self, calc_type):			# calc_type indicates whether this is for rref calcualtions or inverse calcualtions

		i = 1
		m = self.number_rows			# for concision purposes
		n = self.number_columns


		# check if there's zero rows and if the length of the rows are in a descending order
		self.check_zero_rows()
		self.check_length_rows()

		while i < self.nonzero_rows:			# for all nonzero rows

			# if the two adjacent rows have the same length
			# cancel out the pivot value of the lower row by subtracting a multiple of the higher row from it
			if self.len_check(i) == self.len_check(i-1):
				# calculate the ratio between the pivots of the two rows			
				if calc_type == "inverse_calc":			# if this method is run in order to calculate the inverse					
					# the pivot is in position 2*n-self.len_check(i)
					# we need n*2 because the augmented matrix doubles the width of the matrix
					coef = (self.matrix[i][2*n-self.len_check(i)]/self.matrix[i-1][2*n-self.len_check(i)])			
				else:		# if this method is run in order to calculate the rref
					# the pivot is in position n-self.len_check(i)
					coef = (self.matrix[i][n-self.len_check(i)]/self.matrix[i-1][n-self.len_check(i)])

				# subtract a multiple of the higher row from the lower row
				self.matrix[i] = self.matrix[i] - (coef*self.matrix[i-1])			
				
				# check if there's zero rows and if the length of the rows are in a descending order
				self.check_zero_rows()
				self.check_length_rows()
			
			# if the two adjacent rows do not have the same length
			# move on to the next row
			else:
				i += 1

		# cancel out all nonzero values after the pivot by subtracting multiples of all other shorter rows from that row
		for i in range(self.nonzero_rows):			# for all nonzero rows, each row denoted row(A)
			for j in range(i+1, self.nonzero_rows):		# for all rows beneath the row(A) (that are shorter in length)
				for z in range(1,n):						# a constant that runs through all potential number of entries
					if self.len_check(i) == (self.len_check(j) + z):	# for all rows shoter than row(A)
						
						# calculate the ratio between the two entries in the column correspongding to the pivot column of the shorter row
						if calc_type == "inverse_calc":			# if this method is run in order to calculate the inverse
							# the column is in position 2*n+z-self.len_check(i)]/self.matrix[j]
							# we need n*2 because the augmented matrix doubles the width of the matrix
							coef = (self.matrix[i][2*n+z-self.len_check(i)]/self.matrix[j][2*n+z-self.len_check(i)])
						else:	# if this method is run in order to calculate the rref
							# the column is in position n+z-self.len_check(i)]/self.matrix[j]
							coef = (self.matrix[i][n+z-self.len_check(i)]/self.matrix[j][n+z-self.len_check(i)])

						# subtract a multiple of the shorter row from the longer row
						self.matrix[i] = self.matrix[i] - (coef*self.matrix[j])			
					
		# now all that's left are nonzero pivots
		# divide each row by its pivot value so that all leading nonzero entries become 1
		for i in range(self.nonzero_rows):			#for all nonzero rows
			if calc_type == "inverse_calc":
				# the pivot is in position 2*n-self.len_check(i)
				# we need n*2 because the augmented matrix doubles the width of the matrix
				self.matrix[i] = self.matrix[i]/(self.matrix[i][2*n-self.len_check(i)])
			else:
				# the pivot is in position n-self.len_check(i)
				self.matrix[i] = self.matrix[i]/(self.matrix[i][n-self.len_check(i)])

		# for all values, round the answers so that the decimals do not get too lengthy
		for i in range(m):
			if calc_type == "inverse_calc":
				# we need n*2 because the augmented matrix doubles the width of the matrix
				for j in range(2*n):
					self.matrix[i][j] = round(self.matrix[i][j],3)
					# because array calcualtions leave -0 as -0, we convert it to 0 instead
					if self.matrix[i][j] == -0:
						self.matrix[i][j] = 0
			else:
				for j in range(n):
					self.matrix[i][j] = round(self.matrix[i][j],3)
					# because array calcualtions leave -0 as -0, we convert it to 0 instead
					if self.matrix[i][j] == -0:
						self.matrix[i][j] = 0
					
		# return the result directly if the user chooses the rref calculation
		if calc_type == "rref":
			return self.matrix
		
		# if the user chooses to do the inverse calculation
		elif calc_type == "inverse":
			if m != n:				# if the matrix is not a square matrix, it is not invertible
				return "The matrix is not invertible."
			
			else:
				# if the matrix is a square matrix but its rref is not I, it is not invertible
				# check to see if the rref is I
				one_count = 0
				for i in range(m):
					if self.matrix[i][i] == 1:		# check through the diagnal entries to see if each entry is 1
						one_count += 1
				if one_count != m:			# if not all diagnal entries are 1 (if the rref of the matrix is not I)
					return "The matrix is not invertible."

				# if the rref is I, the matrix is invertible
				else:				
					# augment the identity matrix to the matrix
					augmented=[]
					for x,row in enumerate(self.matrix_reference):
						augmented.append(np.array(list(row)+list(self.identity[x])))
					self.matrix=np.array(augmented)

					# run through the function again, this time doing the inverse_calc with the indentity matrix augmented
					return self.calc("inverse_calc") 
		
		# if it is indicated that the method is doing inverse_calc
		else:
			return self.matrix[:m,m:]			# return only the augmented identity matrix

