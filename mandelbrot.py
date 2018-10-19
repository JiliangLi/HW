
from PIL import Image
import random

imgx, imgy = 513, 513

image = Image.new("RGB",(imgx,imgy))

coordinate = []
values = []
count = 0

color1 = (0,0,0)
color2 = (20,20,20)
color3 = (40,40,40)
color4 = (60,60,60)
color5 = (80,80,80)
color6 = (100,100,100)
color7 = (120,120,120)
color8 = (140,140,140)
color9 = (180,180,180)
color10 = (200,200,200)
color11 = (220,220,220)
color12 = (240,240,240)
color13 = (255,255,255)
color14 = (240,240,240)
color15 = (220,220,220)
color16 = (200,200,200)
color17 = (180,180,180)
color18 = (180,180,180)

def mandelbrot(a,b):
	global color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12, color13, color14, color15, color16, color17, color18, re_coef, ima_coef, count, check
	if count > 16:
		return color18



	if (a**2 + b**2) >= 4:

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
		elif count == 6:
			return color7
		elif count == 7:
			return color8
		elif count == 8:
			return color9
		elif count == 9:
			return color10
		elif count == 10:
			return color11
		elif count == 11:
			return color12
		elif count == 12:
			return color13
		elif count == 13:
			return color14
		elif count == 14:
			return color15
		elif count == 15:
			return color16
		elif count == 16:
			return color17
	count += 1
	return mandelbrot((a**2 - b**2 + re_coef), (2*a*b + ima_coef))




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
