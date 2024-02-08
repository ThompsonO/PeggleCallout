import peggle_callout
import keyboard

#callout_filename ='callout.txt'
#callout_text = 'Shotcaller: '

while True:
    # If user presses Shift+Backspace, automatically end the program
    if keyboard.is_pressed('shift+backspace'):
        exit()

    #Take screenshot
    if keyboard.is_pressed('c'):
        can_fire = peggle_callout.can_fire()

        if can_fire:
            print('FIRE!!!!!')
        else:
            print('WAIT!!!!!!')
