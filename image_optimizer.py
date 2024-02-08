import PIL
from PIL import Image
import os

def image_optimizer(path, quality):
    img = Image.open(path)
    #Resize and compress image
    img = img.resize(img.size, PIL.Image.Resampling.LANCZOS)
    #Replace old image with optimization and lower quality
    img.save(path, optimize=True, quality=quality)

def get_images_current_directory():
    current_directory = os.getcwd()
    image_names = []
    #Check every file
    for filename in os.listdir(current_directory):
        #Check if file is iamge (.jpg, .png , ...)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            #Add to array
            image_names.append(filename)
    return image_names

if (__name__ == '__main__'):
    images = get_images_current_directory()
    img_count = 0
    for image in images:
        image_optimizer(image, 90)
        img_count+=1

    print('Completed Optmizations: ' + str(img_count))
    print('Press Key to quit: ')
    input()
    