import numpy as np

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

m = dimension[0]
n = dimension[1]

rows = []
matrix_list = [[0 for i in range(n)]for i in range(m)]
for i in range(m):
		position = "row "+str(i+1)
		rows.append(position)
		print("Please enter the values of the entries in "  + position+ " (separated by space): ")
		rowi = input()
		rowi = rowi.split()
		matrix_list[i] = rowi

for i in range(m):
	for j in range(n):
		matrix_list[i][j] = float(matrix_list[i][j])
		
matrix_array = np.array(matrix_list)

def check_zero_rows():
	global matrix_list, matrix_array, m, n, nonzero_rows
	zero_count = 0;
	count = 0
	while count < nonzero_rows:
		if np.all(matrix_array[count] == 0) == True:
			row_moved = matrix_array[count]
			matrix_array = np.delete(matrix_array, (count), axis = 0)
			zero_count += 1
			nonzero_rows -= 1
			# number_row_moved += 1
		else:
			count += 1
	for i in range(zero_count):
		matrix_array = np.append(matrix_array, [row_moved], axis = 0)

# number_row_moved = 0
nonzero_rows = m

check_zero_rows()

for j in range(n-1):
	number_row = j + 1
	while number_row < nonzero_rows:
		matrix_array[number_row] = matrix_array[number_row] - ((matrix_array[number_row][j]/matrix_array[j][j])*matrix_array[j])
		number_row += 1
		check_zero_rows()
		print(nonzero_rows)
# for i in range(2, m):
# 	matrix_array[i] = matrix_array[i] - ((matrix_array[i][1]/matrix_array[1][1])*matrix_array[1])
# check_zero_rows()

print(matrix_array)

# numbers = [float(x.strip()) for x in input_list]

# thisdict #python dictionaries 

# addition
# subtraction
# div
# mul

# 
