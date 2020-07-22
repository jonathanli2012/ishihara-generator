from PIL import Image, ImageDraw, ImageFont
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

fontname = resource_path('Heebo-Bold.ttf')
fontsize = 300
font = ImageFont.truetype(fontname, fontsize)

def longest_word(s):
    return max(s.split(' '), key=len)

lines = int(input("lines: "))
txt = ""

for i in range(0, lines):
    prompt = "text for line " + str(i+1) + ": "
    txt += input(prompt)
    if(i < lines - 1): txt += "\n"

tmp_img = Image.new('RGB', (1, 1), color = (255,255,255))
d = ImageDraw.Draw(tmp_img)
x_len, y_len = d.textsize(txt, font=font)

img = Image.new('RGB', (x_len+100, y_len+40), color = (255,255,255))

d = ImageDraw.Draw(img)

d.text((50,0), txt, font=font, fill=(0,0,0))
img.save('asset.png')