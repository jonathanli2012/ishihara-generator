from PIL import Image, ImageDraw 
import random
from detect import *
from draw_circle import *
from gen_circles import *

size_x = 600
size_y = 600
min_rad = 4
max_rad = 8
total_circles = 1800

red_green_colors_bkg = ["#f9b409","#e1625d","#f09c80","#f3d3ad","#f8d905"]
red_green_fake_colors = ["#abd284", "#9cb651", "#d6db89"]
mask_img = Image.open("cancel.png")

image = Image.new(mode='RGB', size=(size_x, size_y), color='white')
i=0
while(i < total_circles*0.75):
    circle = gen_circle(size_x, size_y, min_rad, max_rad)
    if(is_free_space(image,circle[0],circle[1],circle[2], size_x, size_y)):
        if(in_mask(mask_img,circle[0],circle[1])):
            draw_circle(image, get_circle_coordinates(circle[0],circle[1],circle[2]), random.choice(red_green_fake_colors))
        else:
            draw_circle(image, get_circle_coordinates(circle[0],circle[1],circle[2]), random.choice(red_green_colors_bkg))
        print("circle " + str(i))
        i += 1

while(i < total_circles):
    circle = gen_circle(size_x, size_y, min_rad, max_rad - 2)
    if(is_free_space(image,circle[0],circle[1],circle[2], size_x, size_y)):
        if(in_mask(mask_img,circle[0],circle[1])):
            draw_circle(image, get_circle_coordinates(circle[0],circle[1],circle[2]), random.choice(red_green_fake_colors))
        else:
            draw_circle(image, get_circle_coordinates(circle[0],circle[1],circle[2]), random.choice(red_green_colors_bkg))
        print("circle " + str(i))
        i += 1

filename = "my_drawing(1).png"
image.save(filename)