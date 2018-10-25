from PIL import Image
import random
import math
import colorsys

imgx, imgy = 1000, 1000

xa, xb = 1.8, 4.5
ya, yb = -1.4, 1.4


image = Image.new("RGB",(imgx,imgy))


def sine(a,b):
	global coordinate_y, coordinate_x, xcoef_real, coef_imag, count
	
	if count >= 100:
		return (coordinate_y/4,coordinate_x*coordinate_y/4000, coordinate_x/4)

	elif ((a**2+b**2)**0.5) >= 10*math.pi:
		return (count, count, count)

	count += 1
	return sine(math.sin(a)*math.cosh(b) + coef_real, math.cos(a)*math.sinh(b) + coef_imag)


for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1) + ya
	coordinate_y = y
	for x in range(imgx):
		coordinate_x = x
		cx = x*(xb-xa)/(imgx-1) + xa
		count = 0
		coef_real = cx
		coef_imag = cy
		(r, g, b) = sine(0,0)
		if count < 100:
			for i in range(0, 256, 5):
				if r+g+b <= i:
					r -= 20*(i/5)
					g += 20*(i/7)
					b += 20*(i/3)
					break

		image.putpixel((x, y),(int(r), int(g), int(b)))

image.save("sine.png", "PNG")