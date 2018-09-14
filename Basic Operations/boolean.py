#sep 13, 2018
#determine if the values are ascending or descending
#sources: python notes http://thomas-cokelaer.info/tutorials/python/boolean.html
import sys
import math

true = float(sys.argv[1])  <  float(sys.argv[2])  <  float(sys.argv[3]) or float(sys.argv[3])  <  float(sys.argv[2])  <  float(sys.argv[1])

print (true)