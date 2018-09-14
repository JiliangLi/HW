#sep 13, 2018
#calculating the wind chill from termperature and wind speed

import sys
w  =  35.74  +  (0.6215*float(sys.argv[1]))  +  ((0.4275*float(sys.argv[1]))  -  35.75)*(float(sys.argv[2])**0.16)
print("the wind chill is:",w)