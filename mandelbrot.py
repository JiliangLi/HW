
from PIL import Image
import random

imgx, imgy = 512, 512

image = Image.new("RGB",(imgx,imgy))

coordinate = []
values = []
colors = []
count = 0


for x in range(256):
	colors.append([x, x, x])


def mandelbrot(a,b):
	global re_coef, ima_coef, count, colors
	
	if count >= 255:
		return (colors[255][0], colors[255][1], colors[255][2])

	elif (a**2 + b**2) >= 4:
		x = count
		return (colors[x][0], colors[x][1], colors[x][2])

	count += 1
	return mandelbrot((a**2 - b**2 + re_coef), (2*a*b + ima_coef))




for i in range(imgy):
	for j in range(imgx):
		coordinate.append([j,i])

for x in range(imgy):
	for y in range(imgx):
		values.append([-2+(y/127.75), 2-(x/127.75)])

for k in range(512*512):
	re_coef = values[k][0]
	ima_coef = values[k][1]
	count = 0
	color = mandelbrot(re_coef,ima_coef)
	image.putpixel((coordinate[k][0], coordinate[k][1]),color)

image.save("mandelbrot.png", "PNG")
