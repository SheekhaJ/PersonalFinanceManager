from PIL import Image
import pytesseract
import cv2
import os.path

if __name__ == '__main__':
    fileName = 'question'
    extension = 'png'
    path = '.\\images\\'

    path = path+fileName+'.'+extension
    im = cv2.imread(path, cv2.IMREAD_COLOR)

    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(im, config=config)
    print('extracted text is ',text)