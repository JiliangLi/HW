#sep 13, 2018
#accepting a date as input and writing the day of the week on which  hat date falls

import sys
import math

month = int(sys.argv[1])
day = int(sys.argv[2])
year = int(sys.argv[3])

y  =  year  -  (14  -  month)  //  12
x  =  y  +  y//4  -  y//100  +  y//400
m  =  month +  12  *  ( (14  -  month)  //  12) -  2
d  =  (day  +  x  + 31*m//  12) %  7  

if (d==0) : print('Sunday')
if (d==1) : print('Monday')
if (d==2) : print('Tuesday')
if (d==3) : print('Wednesday')
if (d==4) : print('Thursday')
if (d==5) : print('Friday')
if (d==6) : print('Saturday')