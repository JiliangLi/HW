from PIL import Image
import math
import colorsys

xa, xb = 0.3025074005126953, 0.3064098358154297
ya, yb = 0.021409034729003906, 0.02531147003173828

imgx, imgy = 1024, 1024

maxIt = 256

image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1) + ya
	for x in range(imgx):
		cx = x*(xb-xa)/(imgx-1) + xa
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c

		h, l, s = math.sin(i), (i*3)%100, i%100

		(r, g, b) = colorsys.hls_to_rgb(h, l, s)
		
		colors = (int(r), int(g), int(b))


		image.putpixel((x,y),colors)

image.show()
image.save("mandelbrot_demo.png", "PNG")
