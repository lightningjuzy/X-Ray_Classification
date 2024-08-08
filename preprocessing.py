import cv2 as cv
import os
import numpy as np
from tqdm import tqdm

'''Trial Processing'''
# img = cv.imread('Data/test/COVID19/COVID19(460).jpg')
# # cv.imshow('Test Image', test)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(gray.shape)
# resized = cv.resize(gray, (256, 256), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)
# print(resized.shape)

'''Loop over all images in Data folder'''
def gray_resize(path):
    img = cv.imread(path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    resized = cv.resize(gray, (256, 256), interpolation=cv.INTER_AREA)
    return resized

def save_image(path, processed_image):
    return cv.imwrite(path, processed_image)


def image_processing():
    '''
    1. Set up the paths to the source and destination folders.
    2. Create list of all the folders in the 'Data/test' folder.
    3. Loop over the list and get the image paths.
    4. Load the image using opencv.
    5. Do the following image processing: Grayscale -> resize -> crop (?)
    6. Save the images into the destination folder
    '''
    source_dir = r'Data'
    save_dir = r'Data_Processed'
    datasets = [i for i in os.listdir(r'Data')]
    for folder in datasets:
        split = os.path.join(source_dir, folder)
        # print(split)
        classes = [c for c in os.listdir(split)]
        # print(classes)
        for i in range(len(classes)):
            current_class = classes[i]
            path = os.path.join(split, current_class)
            # print(path)
            print(f'Processing Images from Folder: {path}')
            for img in tqdm(os.listdir(path)):
                img_path = os.path.join(path, img)
                filename = os.path.basename(img_path)
                # print(img_path)
                resized_img = gray_resize(img_path)
                saving_folder = os.path.join(save_dir, folder, current_class, filename)
                # cv.imwrite(saving_folder, resized_img)
                save_image(saving_folder, resized_img)

def main():
    to_train = 0
    if to_train == 1:
        image_processing()
    else:
        return

main()

'''Verification'''
# Pull a random image
DIR = r'Data_Processed\train\NORMAL\IM-0133-0001.jpeg'
verification_image = cv.imread(DIR)
cv.imshow('Verification Image', verification_image)
print(f'Shape of the image is {verification_image.shape}')

gray = cv.cvtColor(verification_image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)
print(f'Shape of Image after grayscaling is {gray.shape}')

cv.waitKey(0)