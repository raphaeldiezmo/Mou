"""
Name:       AppBot Class
Details:    This app bot class gives out the artificial intelligence
            of a certain simple instructions, this class contains
            automated input methods such as mouse inputs and keyboard inputs
            this also depends on the user's setup instructions
Author:     Raphael Di Ezmo
"""

import cv2 as cv
import pyautogui
from time import sleep, time
from threading import Thread, Lock


class AppBot:

    # AppBot Properties
    target_positions    = []    # this will contain the positions of the matched targets(x,y)
    wincap              = None  # The window capture class
    window_offset       = (0,0) # The window capture's offset
    window_w            = 0     # the window capture's width
    window_h            = 0     # the window capture's height

    # Threading Properties
    stop            = False

    # Constructor, this construct the class AppBot object that contains the window's
    # offset of the targeted window and as well as it's window size
    def __init__(self, window_offset, window_size):
        # For checking window position in the screen position, it'll be easier
        # to just get the offsets and the actual window size from the Window
        # Capture
        self.window_offset  = window_offset     # Initializing the window's offsets
        self.window_w       = window_size[0]    # Initializing the window's width
        self.window_h       = window_size[1]    # Initializing the window's height

    # Getting all the possible target positions (x,y)
    def get_target_positions(self, target_positions):
        self.target_positions = target_positions

    # Iterate to all the target positions
    def get_all_target_pos(self):


        for target in self.target_positions:
            xPos = target[0]
            yPos = target[1]

            # Calling the method click object
            self.clickObject(xPos, yPos)

    # This inputs the clicking action in the targeted window using the
    # x and y inputs
    def clickObject(self, x, y):
        # If x exist and not a null value
        if x:
            # xPos, yPos = self.get_screen_position(target_pos)
            # For Debugging purposes
            print("moving to the {} {}".format(x, y))
            print(pyautogui.position())

            # Mouse pointer moves to the given x and y axis
            pyautogui.moveTo(x, y)
            # Clicking the targeted position using right click button
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # position = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.
    def get_screen_position(self, position):
        return (position[0] + self.offset_x, position[1] + self.offset_y)

    # This updates the position of the mouse
    def update_position(self, x, y):
        self.x_target = x
        self.y_target = y

    # Method that will start the threading
    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    # Method that will stop the function of the thread
    def stop(self):
        self.stopped = True

    # Method that runs all the functionality of the AppBot
    def run(self):
        while not self.stopped and self.x_target != 0 and self.y_target != 0:
            # Inputs the action to the updated x and y target
            self.clickObject(self.x_target, self.y_target)

