# Sep 27, 2018
# source: StackOverflow https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python
# Generate  a  random  list  with  its  items  being  integer  from  1  to  30,  
# the  list  should  be  30  items  long.  
# then  print  only  those  values  whose  digit  sum  equals  5.

import random as r

nums = []
finalnums = []

while len(nums) < 30:
	number = r.randrange(1,31)
	nums += [number]

	digit = [int(x) for x in str(number)]

	if sum(digit) != 5:
		finalnums += [number]

print(nums)
print(finalnums)



