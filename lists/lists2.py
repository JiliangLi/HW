# sep 27, 2018
# source: PythonbyProgramiz https://www.programiz.com/python-programming/list-comprehension
# Generate  a  list  of  100  numbers,  1  to  100,  without  using  a  traditional  looping  technique  (investigate  list  comprehensions).  
# Shuffle  the  list  up  so  the  numbers  are  not  in  order.

import random

numbers = [x for x in range(1,101)]          #list comprehension

random.shuffle(numbers)

print(numbers)

