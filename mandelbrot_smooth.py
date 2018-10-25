from PIL import Image
import random
import math
import colorsys

imgx, imgy = 1000, 1000

xa, xb = 0.3025074005126953, 0.3064098358154297
ya, yb = 0.021409034729003906, 0.02531147003173828


image = Image.new("RGB",(imgx,imgy))


def mandelbrot(z):
	global constant, count
	
	if count >= 256:
		return (0,0,0)

	elif abs(z) >= 2:
		if count > 100:
			count = count - math.log(math.log(abs(z)))/math.log(2)
			return (count-(y/2), count+((y-x)/4), count+(x/2))
		else:
			count = count - math.log(math.log(abs(z)))/math.log(2)
			return (count, count, count)

	count += 1
	return mandelbrot(z**2+constant)

for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1) + ya
	for x in range(imgx):
		cx = x*(xb-xa)/(imgx-1) + xa
		count = 0
		constant = complex(cx, cy)
		(r, g, b) = mandelbrot(0)

		image.putpixel((x, y),(int(r),int(g),int(b)))


image.save("mandelbrot2.png", "PNG")

