# oct 14, 2018
# a program that draws an image algorithmically


from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx,imgy))

red = 255
reference = 0
green = 0
blue = 0

for x in range(512):
	for y in range(512):
		image.putpixel((x,y),(red,green,blue))
		if red == 255 or red == 0:
			reference += 1

		if reference % 2 == 1:
			red -= 3
			green += 3
			blue += 3

		else:
			red += 3
			green -= 3
			blue -= 3

image.save("image.png", "PNG")


