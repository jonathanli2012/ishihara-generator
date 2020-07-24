import random
from PIL import Image, ImageDraw 

class circle:
    @staticmethod
    def generate(sizex,sizey, min_rad, max_rad):
        x = random.randint(min_rad, sizex - min_rad)
        y = random.randint(min_rad, sizey - min_rad)
        radius = random.randint(min_rad, max_rad)
        return [x,y,radius]

    @staticmethod
    def get_coordinates(x, y, radius):
        return [x-radius,y-radius,x+radius,y+radius]

    #Attribution to github/franciscouzo
    @staticmethod
    def is_free_space(image, x, y, r, size_x, size_y):
        points_x = [x, x, x, x-r, x+r, x-r*0.93, x-r*0.93, x+r*0.93, x+r*0.93]
        points_y = [y, y-r, y+r, y, y, y+r*0.93, y-r*0.93, y+r*0.93, y-r*0.93]

        for x in points_x:
            if x >= size_x - 1 or x <= 0: return False
        for y in points_y:
            if y >= size_y - 1 or y <= 0: return False
        for xy in zip(points_x, points_y):
            if image.getpixel(xy)[:3] != (255, 255, 255):
                return False
        return True

    #Attribution to haken.no
    @staticmethod
    def draw(image, bounds, color, antialias=4):
        """Improved ellipse drawing function, based on PIL.ImageDraw."""

        # Use a single channel image (mode='L') as mask.
        # The size of the mask can be increased relative to the imput image
        # to get smoother looking results. 
        mask = Image.new(
            size=[int(dim * antialias) for dim in image.size],
            mode='L', color='black')
        draw = ImageDraw.Draw(mask)

        # draw outer shape in color
        left, top = [value * antialias for value in bounds[:2]]
        right, bottom = [value * antialias for value in bounds[2:]]
        draw.ellipse([left, top, right, bottom], fill='white')

        # downsample the mask using PIL.Image.LANCZOS 
        # (a high-quality downsampling filter).
        mask = mask.resize(image.size, Image.ANTIALIAS)
        # paste outline color to input image through the mask
        image.paste(color, mask=mask)