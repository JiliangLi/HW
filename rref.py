import numpy as np

while True:
	try:
		print("Please enter the dimension of the matrix: \n(for instance, if the matrix is a 2 by 5 matrix, enter 2*5)")
		dimension_raw = input()
		dimension = dimension_raw.split('*')
		dimension[0] = int(dimension[0])
		dimension[1] = int(dimension[1])
		if len(dimension) == 2:
			break
		else:
			print("please enter a valid dimension connected by '*'")

	except ValueError:
		print("Please enter a valid dimension connected by '*'")

m = dimension[0]
n = dimension[1]

matrix_list = [[0 for i in range(m)]for i in range(n)]
for i in range(m):
	for j in range(n):
		position = "v"+str(i+1)+str(j+1)

		matrix_list[i][j] = input("Please enter the value of entry "  + position+ ": ")

print(matrix_list)
		
for i in range(m):
	ri = np.array(matrix_list[m])
print(r2)
# numbers = [float(x.strip()) for x in input_list]
