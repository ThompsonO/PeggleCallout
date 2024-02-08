# PeggleCallout

PeggleCallout is a neural network trained on 17,000 images across all 55 levels of Peggle Deulxe used to determine if the player can fire a ball or not.

This project was originally designed to work with DougDoug, et al's TwitchPlays code available on DougDoug's website: https://www.dougdoug.com/twitchplays

(DougDoug, et al should not be considered affiliated with, nor endorsing the development of this project)

The TwitchPlays code is not necessary to run this project, but examples will be structured based on that project.

## Requirements
This project has been tested on python 3.10.5 and 3.10.6 and all additional packages were installed with the 'pip install' command
The following packages are required to run this project:

```
numpy
opencv-contrib-python
pillow
pywin32
tensorflow
```

## Setup
Download this project inside the repository where the main python script will run.

Add the following to your main script's imports

```from PeggleCallout import peggle_callout```

The `can_fire()` function returns a True/False value based on whether the neural network determines if the player can fire a ball or not.
If you plan on using this to help manage control flow and callout users who activate the fire command with Twitch chat commands then your code may look similar to the following:

```
#This would be in handle_message() in DougDoug's TwitchPlays code

  if msg == 'shoot':

    #It may also be advantageous to add a random chance that the shoot command has a smaller percentage chance to fire
    #add that check here and indent the lines below

    if peggle_callout.can_fire():
          callout_filename = 'callout.txt'
          callout_text = 'Shotcaller: '

          callout_file = open(callout_filename, "w")
          callout_file.write(callout_text + username)
          callout_file.close()

          pydirectinput.mouseDown(button="left")
          time.sleep(0.5)
          pydirectinput.mouseUp(button="left")
```

Then just add the callout.txt file as a text source in your stream management software of choice

It is also recommended to add a Claude Claws Clause so that Twitch chat can still flip Claude's Claws when they are available.  All that is required is a negation of the `can_fire()` function.
Just add this immediately after the above block of code

```
  if msg == 'flip':
      if not peggle_callout.can_fire():
          pydirectinput.mouseDown(button="left")
          time.sleep(0.5)
          pydirectinput.mouseUp(button="left")
```

## Usage
- Have Peggle Deluxe running.
- Then launch your script utilizing PeggleCallout from the command line.
  - You may see informational messages about missing cuda dll files.  This is just a warning that the neural network is running on your cpu instead of gpu and can be ignored. If you wish to run this on your Nvidia gpu instead, researching running tensorflow cuda dll files should be helpful and improve performance, but this has not been tested and is done at the developer's discretion.
- Enjoy!

## How it works
- The `can_fire()` function first takes a snapshot of the Peggle window, resized the window to scale it down, and then crops the image so only an area around the firing cannon remains.
- That image is then fed into the already trained neural network which returns how confident it is the image represents if the player can fire a ball.
- The `can_fire()` function then returns that confidence value as True if a player can fire and False otherwise.

## License
This project is released under the MIT License:
https://opensource.org/licenses/MIT
