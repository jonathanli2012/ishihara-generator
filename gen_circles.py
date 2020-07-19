import random

#Attribution to github/franciscouzo
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

def gen_circle(sizex,sizey, min_rad, max_rad):
    x = random.randint(min_rad, sizex - min_rad)
    y = random.randint(min_rad, sizey - min_rad)
    radius = random.randint(min_rad, max_rad)
    return [x,y,radius]
