
def in_mask(image, x, y):
    if x >= image.size[0] or y >= image.size[1]: return False
    if image.getpixel((x,y))[:3] != (255, 255, 255):
        return True
    return False