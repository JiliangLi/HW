# oct 1, 2018
# this is the minesweeper step 1
# The user  provide  the  width  (W)  and  the  height  (H)  for  the  program
# as  well  as  the  number  of  bombs  on  the  board.  
# The  bombs  (B)  will  be  randomly  placed,  
# and  then  the  program  determines  how  many  bombs  surround  each  space. 

import sys
import random

row = sys.argv[2]
column = sys.argv[1]
b = sys.argv[3]
count = 0
row_count = 1
column_count = 0


field = [[0]*int(column) for x in range(int(row))]



while count < int(b):
	x = random.randrange(0, int(column))
	y = random.randrange(0, int(row))
	field[y][x] = "*"
	count += 1

for j in range(int(row)):
	field[j] += [0]
	field[j] = [0] + field[j]

field = [[0]*(int(column)+2)] + field
field = field + [[0]*(int(column)+2)]

while row_count < (int(row)+1):
	for k in range(1, int(column)+1):
		if field[int(row_count)][k] == "*":
			pass
		else:
			if field[int(row_count)+1][k] == "*":
				field[int(row_count)][k] += 1

			if field[int(row_count)-1][k] == "*":
				field[int(row_count)][k] += 1

			if field[int(row_count)][k+1] == "*":
				field[int(row_count)][k] += 1

			if field[int(row_count)][k-1] == "*":
				field[int(row_count)][k] += 1

			if field[int(row_count)+1][k+1] == "*":
				field[int(row_count)][k] += 1

			if field[int(row_count)+1][k-1] == "*":
				field[int(row_count)][k] += 1

			if field[int(row_count)-1][k+1] == "*":
				field[int(row_count)][k] += 1

			if field[int(row_count)-1][k-1] == "*":
				field[int(row_count)][k] += 1

	row_count += 1



for j in range(int(row)+2):
	field[j].pop(0)
	field[j].pop((int(column)))


for i in range(1, int(row)+1):
		print(*field[i])
