from PIL import Image
import os 

img_path = "images/inquiline_kea.jpg"

kea_img = Image.open(img_path)
kea_img.show()
kea_grayed = kea_img.convert("L")
pixels = list(kea_img.getdata())
print(pixels)


t1 = 50
# t2 = 50
# t3 = 100
# t4 = 32

filtered_pixels_v1 = [pixel if pixel > t1 else 0 for pixel in pixels]
# compressed_v2 = [n if n > e2 else 0 for n in v]

filtered_image = Image.new("L", image.size) # make empty image of same size (num pixels)
filtered_image.putdata(filtered_pixels_v1)
filtered_image.show()