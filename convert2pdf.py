from PIL import Image
import cv2
import numpy as np
from clearimg import *
from allImage import *


imagelist = [imgpil2,imgpil3]
""" cv2.imshow('imgcv2', imgcv2)
im = imgpil2.save('hello.jpg')
cv2.waitKey() """
imgpil1.save(r'E:\WEB_APP\img2pdf\img2pdf.pdf',save_all=True, append_images=imagelist, quality = 95)


