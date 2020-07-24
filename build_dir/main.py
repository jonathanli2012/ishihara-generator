from TextToImage import *
from run import *
from colors import *

print("Text to Ishihara Generator")
result = TextToImage.run_tti()
if(result):
    print("Text Recorded")
else:
    print("Error")
    exit()

dots = input("input number of dots (suggested 1600): ")
dots = int(dots)
run_draw('asset.png', colors.plate_2_bkg, colors.plate_2_txt, dots)
