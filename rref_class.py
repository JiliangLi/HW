import numpy as np

# class Row:
# 	def __init__(self, arr):
# 		self.arr = np.array(arr)

# 		def add(self, other):
# 			self.arr+=other.arr
# 		def sub(self, other):

class Matrix:
	def __init__(self, main_matrix, number_rows, number_columns):
		self.matrix = np.array(main_matrix)
		self.nonzero_rows = number_rows
		self.zero_count = 0
		self.total_row_swapped = 0
		self.number_columns = number_columns
		self.number_rows = number_rows

	def check_zero_rows(self):
		self.zero_count = 0;
		count = 0
		while count < self.nonzero_rows:
			if np.all(self.matrix[count] == 0) == True:
				row_moved = self.matrix[count]
				self.matrix = np.delete(self.matrix, (count), axis = 0)
				self.zero_count += 1
				self.nonzero_rows -= 1
				self.total_row_swapped += 1
			else:
				count += 1
		for i in range(self.zero_count):
			self.matrix = np.append(self.matrix, [row_moved], axis = 0)

		# return self.matrix

	def len_check(self,row):
		row_check = self.matrix[row]
		column_remaining = self.number_columns

		j = 0
		while j < column_remaining:
			if row_check[j] != 0:
				break
			elif row_check[j] == 0:
				row_check = np.delete(row_check, j)
				column_remaining -= 1
		return len(row_check)

	def check_length_rows(self):
		# global nonzero_rows, matrix_array, row_length, rows_swapped, total_row_swapped

		matrix_check = self.matrix
		rows_swapped = 0
		row_length = []
		for i in range(self.nonzero_rows):
			row_length.append(self.len_check(i))

		i = 0
		while i < (self.nonzero_rows-1):
			if row_length[i+1] > row_length[i]:
				# print(row_length[i], row_length[i+1])
				# print(matrix_array[i], matrix_array[i+1])
				row_length[i], row_length[i+1] = row_length[i+1], row_length[i]
				self.matrix[[i,i+1]] = self.matrix[[i+1,i]] 
				rows_swapped += 1
				# print(row_length[i], row_length[i+1])
				# print(matrix_array[i], matrix_array[i+1])
			i += 1

		if rows_swapped != 0:
			self.total_row_swapped += 1

	def calc(self, type):
		self.check_zero_rows()
		self.check_length_rows()
		i = 1
		m = self.number_rows
		n = self.number_columns
		while i < self.nonzero_rows:
			if self.len_check(i) == self.len_check(i-1):
				coef = (self.matrix[i][n-self.len_check(i)]/self.matrix[i-1][n-self.len_check(i)])
				self.matrix[i] = self.matrix[i] - (coef*self.matrix[i-1])
				self.check_zero_rows()
				self.check_length_rows()
			else:
				i += 1


		for i in range(self.nonzero_rows):
			for j in range(i+1, m):
				for z in range(1,n):
					if self.len_check(i) == (self.len_check(j) + z):
						coef = (self.matrix[i][n+z-self.len_check(i)]/self.matrix[j][n+z-self.len_check(i)])
						self.matrix[i] = self.matrix[i] - (coef*self.matrix[j])
					
		for i in range(self.nonzero_rows):
			self.matrix[i] = self.matrix[i]/(self.matrix[i][n-self.len_check(i)])
		
		for i in range(m):
			for j in range(n):
				self.matrix[i][j] = round(self.matrix[i][j],3)
				if self.matrix[i][j] == -0:
					self.matrix[i][j] = 0
		
		matrix_display = list(self.matrix)
		return matrix_display

	def inverse(self):
		self.check_zero_rows()
		self.check_length_rows()
		i = 1
		m = self.number_rows
		n = self.number_columns
		while i < self.nonzero_rows:
			if self.len_check(i) == self.len_check(i-1):
				coef = (self.matrix[i][n-self.len_check(i)]/self.matrix[i-1][n-self.len_check(i)])
				self.matrix[i] = self.matrix[i] - (coef*self.matrix[i-1])
				self.check_zero_rows()
				self.check_length_rows()
			else:
				i += 1


		for i in range(self.nonzero_rows):
			for j in range(i+1, m):
				for z in range(1,n):
					if self.len_check(i) == (self.len_check(j) + z):
						coef = (self.matrix[i][n+z-self.len_check(i)]/self.matrix[j][n+z-self.len_check(i)])
						self.matrix[i] = self.matrix[i] - (coef*self.matrix[j])
					
		for i in range(self.nonzero_rows):
			self.matrix[i] = self.matrix[i]/(self.matrix[i][n-self.len_check(i)])
		
		for i in range(m):
			for j in range(n):
				self.matrix[i][j] = round(self.matrix[i][j],3)
				if self.matrix[i][j] == -0:
					self.matrix[i][j] = 0
		
		matrix_display = list(self.matrix)
		return matrix_display



while True:
	try:
		print("Please enter the dimension of the matrix: \n(for instance, if the matrix is a 2 by 5 matrix, enter 2*5)")
		dimension_raw = input()
		dimension = dimension_raw.split('*')
		if len(dimension) == 2:
			dimension[0] = int(dimension[0])
			dimension[1] = int(dimension[1])
			break
		else:
			print("please enter a valid dimension connected by '*'")

	except ValueError:
		print("Please enter a valid dimension connected by '*'")

rows= []
matrix_list = [[0 for i in range(dimension[1])]for i in range(dimension[0])]
for i in range(dimension[0]):
		position = "row "+str(i+1)
		rows.append(position)
		print("Please enter the values of the entries in "  + position+ " (separated by space): ")
		while True:
			try:
				while True:
					rowi = input()
					rowi = rowi.split()
					if len(rowi) == dimension[1]:
						matrix_list[i] = rowi
						break
					else:
						print("Please create a matrix corresponding to column number " + str(dimension[1])+".")

				for j in range(dimension[1]):
					matrix_list[i][j] = float(matrix_list[i][j])
				break

			except ValueError:
				print("Please enter entries that are real numbers.")

	

matrix1 = Matrix(matrix_list,dimension[0],dimension[1])

for i in range(dimension[0]):
	print(*matrix1.calc(rref)[i])






	# i += 1
# print(nonzero_rows)
# for i in range(nonzero_rows):
# 	if i != m-1:
# 		for j in range(i+1, nonzero_rows):
# 			if matrix_array[j][j] != 0:
# 				# matrix_array[i] = matrix_array[i] - ((matrix_array[i][j]/matrix_array[j][j])*matrix_array[j])
# 				matrix_array[i] = matrix_array[i] - ((matrix_array[i][j]/matrix_array[j][j])*matrix_array[j])

# for i in range(nonzero_rows):
# 	for j in range(i,n):
# 		if j != 0:
# 			matrix_array[i] = matrix_array[i]/matrix_array[i][j]
# 			break
# for i in range(2, m):
# 	matrix_array[i] = matrix_array[i] - ((matrix_array[i][1]/matrix_array[1][1])*matrix_array[1])
# check_zero_rows()
# print(matrix_array)

# numbers = [float(x.strip()) for x in input_list]

# thisdict #python dictionaries 

# addition
# subtraction
# div
# mul

# 
