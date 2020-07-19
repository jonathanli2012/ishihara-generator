from PIL import Image, ImageDraw 

def get_circle_coordinates(x, y, radius):
    return [x-radius,y-radius,x+radius,y+radius]

#Attribution to haken.no
def draw_circle(image, bounds, color, antialias=4):
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
