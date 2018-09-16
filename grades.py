#sep 16, 2018
#a program that accepts from the command line one and only one argument, a float between 0 and 5. 
#if the number is not in the range, the program tells the user that a number between 0 and 5 is expectd, and quits. 
#if the number the user enters is good, the program determines his/her grade in the class.

import sys 

g = float(sys.argv[1])

if len(sys.argv) == 2:

	if 0 >= g or  5 <= g:
		print ("A number between 0 and 5 is expected. Please re-enter the program.")

	else:
		if g >= 4.85:
			print("A+")

		elif g >= 4.7:
			print("A")

		elif g >= 4.5:
			print("A-")

		elif g >= 4.2:
			print("B+")

		elif g >= 3.85:
			print("B")

		elif g >= 3.5:
			print("B-")

		elif g >= 3.2:
			print("C+")

		elif g >= 2.85:
			print("C")

		elif g >= 2.5:
			print("C-")

		elif g >= 2:
			print("D+")

		elif g >= 1.5:
			print("D")

		elif g >= 1:
			print("D-")

		else:
			print("F")

else:
	print("Only one number between 0 and 5 is expected. Please re-enter the program.")