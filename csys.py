from PIL import Image
import colorsys

imgx = 512
imgy = 512	

image = Image.new("RGB", (imgx, imgy))



for x in range(512):
	for y in range(512):
		image.putpixel((x,y),(colorsys.hls_to_rgb(100, 100, 100)))


image.save("csys.png", "PNG")