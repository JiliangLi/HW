# Sep27, 2018
# source: StackOverflow https://stackoverflow.com/questions/9138112/looping-over-a-list-in-python/9138132
# source: PythonbyProgramiz https://www.programiz.com/python-programming/methods/list/sort
# source: Jerry Wang
# Generate  a  list  of  10  random  numbers  between  0  and  100.  
# Get  them  inorder  from  largest  to  smallest,  
# removing  numbers  divisible  by  3.

import random

nums = []
while len(nums) < 10:
	number = random.randrange(0,101)
	nums.append(number)

nums.sort(reverse=True)

print(nums)

i = 0

while i < len(nums):
	if nums[i] % 3 == 0:
		nums.pop(i)
		i -= 1
	i += 1

print(nums)