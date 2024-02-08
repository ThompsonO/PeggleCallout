# installed with 'pip install opencv-contrib-python'
from cmath import exp
from turtle import shape
import cv2 as cv
import numpy as np
import keyboard
import os

verbose = False

def resize(img, filepath):
    global verbose

    # Expected pixel dimensions of image (do not change!)
    expected_shape = (900, 1200, 3)

    if img.shape != expected_shape:
        if verbose:
            print(f'Resizing Image {filepath}: Image shape: {img.shape}, Expected shape: {expected_shape}')
        img = cv.resize(img, (expected_shape[1], expected_shape[0]))

        if verbose:
            print(f'Resize complete! {img.shape}')

    mini = cv.resize(img, (400, 300))
    mini_crop = mini[25:200, 50:350]

    return mini_crop

save_filepath = 'D:/NeuralNetwork/screenshots/'
img_repo = save_filepath + 'Peggle/'
save_repo = img_repo + 'Processed/'
positives = 'can_fire'
negatives = 'no_fire'

if not os.path.isdir(img_repo + positives):
    print('Error: No can_fire data set')
    exit()
if not os.path.isdir(img_repo + negatives):
    print('Error: No no_fire data set')
    exit()

if not os.path.isdir(save_repo):
    os.mkdir(save_repo)
if not os.path.isdir(save_repo + positives):
    os.mkdir(save_repo + positives)
if not os.path.isdir(save_repo + negatives):
    os.mkdir(save_repo + negatives)

can_fire_filepaths = [f for f in os.listdir(
    img_repo + positives) if os.path.isfile(os.path.join(img_repo + positives, f))]

no_fire_filepaths = [f for f in os.listdir(
    img_repo + negatives) if os.path.isfile(os.path.join(img_repo + negatives, f))]

total_images = len(can_fire_filepaths) + len(no_fire_filepaths)
i = 0
print(f'Processing {total_images} images.')

for path in can_fire_filepaths:
    i += 1
    print(f'Processing image {i} of {total_images}', end='\r')

    img = cv.imread(os.path.join(img_repo + positives + '/', path))
    mini = resize(img, os.path.join(img_repo + positives + '/', path))

    cv.imwrite(os.path.join(save_repo + positives + '/', path), mini)


for path in no_fire_filepaths:
    i += 1
    print(f'\rProcessing image {i} of {total_images}', end='\r')

    img = cv.imread(os.path.join(img_repo + negatives + '/', path))
    mini = resize(img, os.path.join(img_repo + negatives + '/', path))

    cv.imwrite(os.path.join(save_repo + negatives + '/', path), mini)
