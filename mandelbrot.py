
from PIL import Image
import random

imgx = 513
imgy = 513

image = Image.new("RGB",(imgx,imgy))

coordinate = []
values = []
count = 0

color1 = (0,0,0)
color2 = (0,0,20)
color3 = (0,0,40)
color4 = (0,0,60)
color5 = (0,0,80)
color6 = (0,0,100)
color7 = (0,0,120)
color8 = (0,0,140)
color9 = (0,0,180)
color10 = (0,0,200)
color11 = (0,0,220)
color12 = (0,0,240)
color13 = (0,0,260)
color14 = (0,0,280)


def mandelbrot(a,b):
	# global color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12, color13, color14, re_coef, ima_coef, count
	global count
	if count > 13:
		return color14

	elif (a**2 + b**2) >= 4:
		if count == 0:
			return color1
		elif count == 1:
			return color2
		elif count == 2:
			return color3
		elif count == 3:
			return color4
		elif count == 4:
			return color5
		elif count == 5:
			return color6
		elif count == 7:
			return color7
		elif count == 8:
			return color8
		elif count == 9:
			return color9
		elif count == 10:
			return color10
		elif count == 11:
			return color11
		elif count == 12:
			return color12
		elif count == 13:
			return color13

	count += 1
	return mandelbrot(a**2 - b**2 + a, 2*a*b + b)




for i in range(513):
	for j in range(513):
		coordinate.append([j,i])

for x in range(513):
	for y in range(513):
		values.append([-2+(y/128), 2-(x/128)])

for k in range(513*513):
	re_coef = values[k][0]
	ima_coef = values[k][1]
	count = 0
	color = mandelbrot(re_coef,ima_coef)
	image.putpixel((coordinate[k][0], coordinate[k][1]),color)

image.save("mandelbrot.png", "PNG")
