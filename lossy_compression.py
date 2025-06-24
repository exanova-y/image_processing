# lossy compression of a coloured image
from PIL import Image
import os 

# show parrot image
img_path = "images/inquiline_kea.jpg"
kea_img = Image.open(img_path)

# split the image into rgb channels
img_channels = []
r_img, g_img, b_img = kea_img.split()
img_channels.append(r_img)
img_channels.append(g_img)
img_channels.append(b_img)

# for each channel for each pixel, apply thresholding
new_img_channels = []
t1 = 80 # you can set this value to be any between 0 to 100

for channel in img_channels:
    pixels = list(channel.getdata()) 

    filtered_pixel_values = [pixel if pixel > t1 else 0 for pixel in pixels] # only keep pixels with value above thresholding
    num_total_pixels = len(filtered_pixel_values)
    num_surviving_pixels = filtered_pixel_values.count(0)
    surviving_ratio = round(num_surviving_pixels/num_total_pixels, 2)
    reduction_ratio = round(1-surviving_ratio, 2)
    print(f"image reduced by {reduction_ratio*100}% among {num_total_pixels} pixels within this channel.")

    filtered_band = Image.new("L", channel.size) # create an empty image of the band
    filtered_band.putdata((filtered_pixel_values)) # putdata function accepts a tuple
    new_img_channels.append(filtered_band)

compressed_img = Image.merge("RGB", new_img_channels) # make empty image of same size (num pixels)
compressed_img.show()