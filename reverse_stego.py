import cv2
import numpy as np
from matplotlib import pyplot as plt

from PIL import Image

img = cv2.imread('source_bmp.bmp', 3)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

img_stego_after = cv2.imread('image_after.bmp', 3)
f_stego = np.fft.fft2(img_stego_after)
fshift_stego = np.fft.fftshift(f_stego)

fshift_logo = fshift_stego - fshift
fshift_logo = fshift_logo * 20

f_ishift = np.fft.ifftshift(fshift_logo)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

cv2.imwrite('logo_after_reverse.bmp', img_back)
Image.open('logo_after_reverse.bmp').save('logo_after_reverse.jpg')
