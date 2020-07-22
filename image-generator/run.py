import random, math, os
from circle import *
from progress.bar import IncrementalBar
from PIL import Image, ImageDraw 
#from colormap import rgb2hex

def in_mask(image, x, y):
    if x >= image.size[0] or y >= image.size[1]: return False
    if image.getpixel((x,y))[:3] != (255, 255, 255):
        return True
    return False

def run_draw(mask_file, plate_bkg, plate_txt, dots=1600, save_all = False):
    mask_img = Image.open(mask_file)
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

    total_circles = dots

    image = Image.new(mode='RGB', size=(size_x, size_y), color='white')

    #from faker import Factory
    #fake = Factory.create()
    bar = IncrementalBar("Drawing Circles", max=total_circles, suffix = '%(percent).1f%% - %(eta)ds')

    i = 0 #counter
    while(i < total_circles):
        new_circle = circle.generate(size_x, size_y, min_rad, max_rad)
        if(circle.is_free_space(image, new_circle[0], new_circle[1],\
            new_circle[2], size_x, size_y)):
            
            coordinates = circle.get_coordinates(new_circle[0],new_circle[1],new_circle[2])

            if(in_mask(mask_img,new_circle[0],new_circle[1]) == False):
                #color = fake.hex_color()
                #plate = random.choice([color])
                plate = random.choice(plate_bkg)
            else:
                #plate = random.choice(["#000000"])
                plate = random.choice(plate_txt)
            
            circle.draw(image, coordinates, mask_img.getpixel((new_circle[0],new_circle[1])))#plate)
            i += 1
            bar.next()
            if(save_all):
                i_str = str(i)
                i_format = i_str.zfill(5)
                filename = "files/run1/" + i_format + ".png"
                image.save(filename)
            
    bar.finish()
    print("Done")
    filename = os.path.splitext(mask_file)[0] + "_ishihara" + ".png"
    
    image.save(filename)