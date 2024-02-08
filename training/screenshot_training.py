import win32gui as pywin
import pyautogui
import time
import datetime
import keyboard
import os

# True if you want to be able to reposition the window while screenshotting
update_coords = True
# Must be filepath friendly
save_folder = 'Peggle/Preprocess/'
positive = 'can_fire/'
negative = 'no_fire/'
# Exact window name
win_name = 'Peggle Deluxe 1.01'
# How often screenshots will be taken (seconds)
screenshot_interval = 0.2

save_filepath = 'D:/NeuralNetwork/screenshots/'
save_filetype = '.png'
screenshot_time = time.time()
frame_coords = ()

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

frame_coords = win_coords(win_name)

if not os.path.isdir(save_filepath + save_folder):
    os.mkdir(save_filepath + save_folder)

if not os.path.isdir(save_filepath + save_folder + positive):
    os.mkdir(save_filepath + save_folder + positive)
if not os.path.isdir(save_filepath + save_folder + negative):
    os.mkdir(save_filepath + save_folder + negative)

time.sleep(1)

fired = False
aiming = False

while True:
    # If user presses Shift+Backspace, automatically end the program
    if keyboard.is_pressed('shift+backspace'):
        exit()

    #Aiming shots
    if keyboard.is_pressed('c'):
        aiming = True
        fired = False

    #Fired shots
    if keyboard.is_pressed('enter'):
        fired = True
        aiming = False
        time.sleep(0.3)

    #Stop all pictures
    if keyboard.is_pressed('m'):
        fired = False
        aiming = False

    #Captuer screenshots
    if fired or aiming:
        if time.time() - screenshot_time > screenshot_interval:
            save_name = ''
            pic_type = ''

            if fired:
                pic_type = 'no_fire'
                save_name = save_filepath + save_folder + negative +\
                    str(datetime.datetime.now().strftime(
                        '%Y-%m-%d-%H-%M-%S.%f')) + save_filetype
            if aiming:
                pic_type = 'can_fire'
                save_name = save_filepath + save_folder + positive +\
                    str(datetime.datetime.now().strftime(
                        '%Y-%m-%d-%H-%M-%S.%f')) + save_filetype

            print(f'{pic_type}: Taking screenshot {datetime.datetime.now()}')
            screenshot_time = time.time()

            if update_coords:
                frame_coords = win_coords(win_name)

            pyautogui.screenshot(save_name, region=(frame_coords))
