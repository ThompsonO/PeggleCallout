# Installed with 'pip install pywin32'
import win32gui as pywin
import pyautogui
# Installed with 'pip install opencv-contrib-python'
import cv2 as cv
from PIL import Image
import numpy as np

# Exact window name
win_name = 'Peggle Deluxe 1.01'
verbose = False

def win_coords(win_title):
    try:
        win = pywin.FindWindow(None, win_title)
        pywin.SetForegroundWindow(win)

        left, top, right, bottom = pywin.GetClientRect(win)
        left, top = pywin.ClientToScreen(win, (left, top))
        right, bottom = pywin.ClientToScreen(
            win, (right-left, bottom-top))

        return (left, top, right, bottom)

    except Exception as e:
        print("Encountered exception: " + str(e))


def capture_win(win_name):
    frame_coords = win_coords(win_name)
    return pyautogui.screenshot(region=(frame_coords))

def pil_to_cv(img):
    cv_img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
    return cv_img

def cv_to_pil(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img)
    return img_pil

def resize(img):
    global verbose

    img = pil_to_cv(img)

    # Expected pixel dimensions of image, do not change! (height, width, 3 channels for rgb)
    expected_shape = (900, 1200, 3)

    if img.shape != expected_shape:
        if verbose:
            print(f'Resizing Image: Image shape: {img.shape}, Expected shape: {expected_shape}')
        img = cv.resize(img, (expected_shape[1], expected_shape[0]))

        if verbose:
            print(f'Resize complete! {img.shape}')

    #Make image smaller (width, height)
    mini = cv.resize(img, (400, 300))
    #Crop to selected area [y1:y2, x1:x2]
    mini_crop = mini[25:200, 50:350]

    mini_crop = cv_to_pil(mini_crop)

    return mini_crop

def screenshot():
    global win_name

    img = capture_win(win_name)
    mini = resize(img)

    return mini

