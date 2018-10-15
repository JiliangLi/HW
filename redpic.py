# oct 14, 2018
# a program that draws an image algorithmically


from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx,imgy))

red = 255
reference = 0
color2 = 0
color3 = 0

for x in range(512):
	for y in range(512):
		image.putpixel((x,y),(red,color2,color3))
		if red == 255 or red == 0 or color2 == 255 or color2 == 0 or color3 == 255 or color3 ==0:
			reference += 1

		if reference % 2 == 1:
			red -= 3
			color2 += 3
			color3 += 3

		else:
			red += 3
			color2 -= 3
			color3 -= 3

image.save("image.png", "PNG")


