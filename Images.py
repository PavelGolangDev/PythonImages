from PIL import Image
import numpy as np
import os
from resizeimage import resizeimage
import cv2
from matplotlib import mlab
import pylab
import math
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

path = '/Users/Pavel/Desktop/images'
fds = sorted(os.listdir(path))
imgballons = "ballons.jpg"
pathballons = "/Users/Pavel/Desktop/images/ballons.jpg"

# Задание 1.3 Чернобелый
def rgb2gray(input_im):
    image_file = Image.open(input_im)
    image_file = image_file.convert('L')
    image_file = image_file.convert('1')
    image_file.save("C:/Users/Pavel/Desktop/imagess/convert"+st+".png")


#Задание 1.3  Разрешение
def downsample(input_im2):
    image_file2 = Image.open(input_im2)
    (h, w) = image_file2.size
    image_file2 = resizeimage.resize_cover(image_file2, (int(h/2), int(w/2)))
    image_file2.save("C:/Users/Pavel/Desktop/imagess/resolution" + st + ".png")

#Задание 1.3 Бинарное
def gray2onebpp(input_im3):
    image_file3 = cv2.imread(input_im3,cv2.IMREAD_COLOR)
    r, threshold_image = cv2.threshold(image_file3, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite("C:/Users/Pavel/Desktop/imagess/binar" + st + ".png", threshold_image)


st="0"
for img in fds:
    if img.endswith(('.jpg', '.png', '.jpeg')):
        st=st+"1"
        print(img,os.path.getsize(os.path.join(path, img)))
        rgb2gray(os.path.join(path, img))
        downsample(os.path.join(path, img))
        gray2onebpp(os.path.join(path, img))

print("   ")
