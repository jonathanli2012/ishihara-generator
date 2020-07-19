def in_mask(image, x, y):
    if image.getpixel((x,y))[:3] != (255, 255, 255):
        return True
    return False