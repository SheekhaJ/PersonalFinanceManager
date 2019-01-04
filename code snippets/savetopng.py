from PIL import Image
import pytesseract
import cv2
import os.path

if __name__ == '__main__':
    fileName = 'support'
    extension = 'jpg'
    path = '.\\images\\'

    image = Image.open(path+fileName+'.'+extension)
    # image.show()
    newExtension = 'png'
    
    if not os.path.exists(path+fileName+'.'+newExtension):
        print('Doesn\'t exist')
        image.save(path+fileName+'.'+newExtension)
    # image.show()