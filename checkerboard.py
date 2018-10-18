# checkerboard

from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx,imgy))

color1 = 0
reference = 0
color2 = 0
color3 = 0

for x in range(512):
	for y in range(512):
		if x in range(0, 64) or x in range(128, 192) or x in range(256, 320) or x in range(384, 448):
			color1 = color2 = color3 = 0
		if x in range(64, 128) or x in range(192, 256) or x in range(320, 384) or x in range(448, 512):
			color1 = color2 = color3 = 255


		if y in range(0, 64) or y in range(128, 192) or y in range(256, 320) or y in range(384, 448):
			if color1 == 0:
				color1 = color2 = color3 = 255
			else:
				color1 = color2 = color3 = 0

		image.putpixel((x,y),(color1,color2,color3))


		# elif y in range(64, 128) or y in range(192, 256) or y in range(320, 384) or y in range(448, 512):
		# 	if color1 == 0:
		# 		color1 = color2 = color3 = 255
		# 	else:
		# 		color1 = color2 = color3 = 0

		# 	color1 = color2 = color3 = 255
		# if y in range(64, 128) or x in range(192, 256) or x in range(320, 384) or x in range(448, 512):
		# 	if color1 == 0:
		# 		image.putpixel((x,y),(255,255,255))
		# 	elif color1 == 255:
		# 		image.putpixel((x,y),(255,255,255))



image.save("checkerboard.png", "PNG")


