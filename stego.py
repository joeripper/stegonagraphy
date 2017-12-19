import numpy as np
import cv2
from PIL import Image

MIN = 100000
MAX = -100000

def open_image(path):
    img = cv2.imread(path, 3)
    if path[len(path)-2:] == 'bmp':
        return(img)
    else:
        cv2.imwrite(path + '.bmp', img)
        img = cv2.imread(path + '.bmp')
        return(img)

def process_image(path_img, path_golo):
    img = open_image(path_img)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    img_golo = open_image(path_golo)
    f_golo = np.fft.fft2(img_golo)
    fshift_golo = np.fft.fftshift(f_golo)
    for i in range(0, 512):
        for j in range(0, 512):
            for m in range(0,3):
                fshift_golo[i][j][m] = fshift_golo[i][j][m]/(20)

    fshift_stego = fshift_golo + fshift
    f_ishift = np.fft.ifftshift(fshift_stego)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    f_ishift_golo = np.fft.ifftshift(fshift_golo)
    img_stego_back = np.fft.ifft2(f_ishift_golo)
    img_stego_back = np.abs(img_stego_back)

    cv2.imwrite(r'/test/test.jpg', img_back)
    cv2.imwrite(r'/test/test_golo.jpg', img_stego_back)

#    Image.open(output_image + 'test.bmp').save(output_image + '.jpg')
#    Image.open(output_image + 'test_golo.bmp').save(output_image + '_golo.bmp')



if __name__ == "__main__":
    open_image('image.jpg')
