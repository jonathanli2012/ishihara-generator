from PIL import Image, ImageDraw 
import random, math
from detect import *
from circle import *
from colors import *


mask_img = Image.open("files/nug1.png")
mask_img = mask_img.convert('RGB')

size_x = mask_img.size[0]
size_y = mask_img.size[1]

min_val = min(size_x,size_y)
min_rad = math.floor(min_val/150)

if(min_rad == 0): min_rad = 1
max_rad = math.floor(min_val/75)
if(max_rad == 0):
    print("IMG Size is too small")
    quit()

total_circles = math.floor(size_x*size_y/800)

plate_bkg = colors.plate_2_bkg
plate_txt = colors.plate_2_txt

image = Image.new(mode='RGB', size=(size_x, size_y), color='white')

i = 0 #counter
while(i < total_circles):
    new_circle = circle.generate(size_x, size_y, min_rad, max_rad)
    if(circle.is_free_space(image, new_circle[0], new_circle[1],\
        new_circle[2], size_x, size_y)):
        
        coordinates = circle.get_coordinates(new_circle[0],new_circle[1],new_circle[2])

        if(in_mask(mask_img,new_circle[0],new_circle[1]) == False):
            plate = random.choice(plate_bkg)
        else:
            plate = random.choice(plate_txt)
        
        circle.draw(image, coordinates, plate)
        print("circle " + str(i) + "/" + str(total_circles))
        i += 1

filename = "my_drawing(2).png"
image.save(filename)