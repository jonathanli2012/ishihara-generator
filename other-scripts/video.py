import cv2
import numpy as np
import glob
"""
img_array = []
for filename in glob.glob('files/run1/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    print(filename)
"""
img_array = []
for count in range(0,1800,6):
    i_str = str(count+1)
    i_format = i_str.zfill(5)
    filename = "files/run1/" + i_format + ".png"
    print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

i_str = str(1800)
i_format = i_str.zfill(5)
filename = "files/run1/" + i_format + ".png"
print(filename)
img_end = cv2.imread(filename)

for count in range(0,30*5):
    img_array.append(img_end)

 
out = cv2.VideoWriter('project_fast.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
 
for i in range(len(img_array)):
    print(i)
    out.write(img_array[i])
out.release()