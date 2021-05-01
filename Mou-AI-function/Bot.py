"""
Name:       AppBot Class
Details:    This app bot class gives out the artificial intelligence
            of a certain simple instructions, this class contains
            automated input methods such as mouse inputs and keyboard inputs
            this also depends on the user's setup instructions
Author:     Raphael Di Ezmo
"""

import cv2 as cv
import pyautogui #pip install pyautogui
from time import sleep, time
from threading import Thread, Lock
from Detector import Detector

# enumerates the application bot status
class AppBotStatus(enumerate):
    INITIALISING    = 0
    DETECTING       = 0
    SEARCHING       = 0
    PROCESSING      = 0
    # only for SD game
    OPENING         = 0

# application bot class
class AppBot:

    # AppBot Properties
    status              = None  # Holds the bot current status
    target_positions    = []    # this will contain the positions of the matched targets(x,y)
    instructions        = []    # this variable will contain the set of instructions
    detector            = None  # detector class that will detects the object
    repeatition         = 0     # variable for a repeatition of an action
    # target in x and y position
    x_target            = 0
    y_target            = 0

    # Window capture properties position
    window_offset       = (0,0) # The window capture's offset
    window_w            = 0     # the window capture's width
    window_h            = 0     # the window capture's height

    # Threading Properties
    stop            = False
    lock            = None

    # Constructor, this construct the class AppBot object that contains the window's
    # offset of the targeted window and as well as it's window size
    def __init__(self, detector, window_offset, window_size, reps):

        # Initialising the Thread lock object
        self.lock = Lock()

        # Getting the initialised detector from the main class
        self.detector = detector

        # For checking window position in the screen position, it'll be easier
        # to just get the offsets and the actual window size from the Window
        # Capture
        self.window_offset  = window_offset     # Initializing the window's offsets
        self.window_w       = window_size[0]    # Initializing the window's width
        self.window_h       = window_size[1]    # Initializing the window's height

        # Initialising status of the appBot
        self.status = AppBotStatus.INITIALISING

        # initializes the repeatition target times
        self.repeatition = reps

    # detects the object and return if the dected object
    def detect(self):
        detected = self.detector.locate()
        return detected

    # re-detection of the target position list and checking if there is the same
    # target positions of the targeted object
    def detecting_new_location(self):
        # initialising arg for the while loop
        arg = True
        # detecting object
        detected = self.detect()
        # while their's no detected items
        while detected == 0:
            # re-detecting the items
            detected = self.detect()

        # loop detecting the target position
        while arg:
            # re-detection of the application scene
            detection = self.detector.locate()
            # if the detection and target position size are the not the same
            # it will check the target position and adds up the latest target position into
            # the last position of the list instead of re-initialising the detection
            if len(detection) != len(self.target_positions):
                for i in range(len(self.target_positions)):
                    for x in range(len(detection)):
                        # once the detected item doesn't match the record
                        if self.target_positions[i] != detection[x]:
                            # adding it up to the current list
                            self.target_positions.append(detection[x])
                            # getting the x and y position
                            x = self.target_positions[-1][0]
                            y = self.target_positions[-1][1]
                            self.right_click_scroll(x,y)
                            # getting out of the loop
                            arg = False
                            break

    # Method on clicking the target position using right click mouse button
    def right_click_sroll(self, x, y):
        print("moving to the {} {}".format(x, y))
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown(button='right')
        pyautogui.mouseUp(button='right')

    # Method on clicking the target position using left click mouse button
    def left_click_scroll(self, x, y):
        print("moving to the {} {}".format(x, y))
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')

    # Method that opens up the targeted object (scrolls)
    # it'll be iterated 10x to open 10 level 3 scrolls
    def open_scrolls(self):

        rep = 1
        # sample instructions -> only works for Supreme Destiny (for now)
        # clicking scrolls 10x
        while rep <= 10:
            # go to the 2nd page inventory
            # set the x and y of the 2nd inventory

            # Clicking the 2nd inventory
            # X AND Y ARE SUBJECTED TO CHANGE
            self.left_click_scroll(x=0,y=0)

            # getting the first located water scroll position
            # doesn't matter where the scroll is since it's going to detect
            # all the scrolls and it'll just pick the first position of the
            # scroll
            get_water = self.detector.locate()
            x = get_water[0][0]
            y = get_water[0][1]
            # open up the scroll
            self.right_click_sroll(x,y)
            # --------------------------------------------------------------------------
            # set the x and y of the 1st inventory
            # Fetching the 1st inventory - since the scroll will re-appear on the 1st invent
            self.left_click_scroll(0,0)

            # -------- re-detection for the new scroll ------------
            self.detecting_new_location()

            # sleeps the bot for 3 seconds
            sleep(3)
            # increments the repeatition
            rep = rep + 1


    # Closes the targeted scroll
    # Parameters
    #   @target         : contains the x and y axis value of the targeted scroll
    #   @num_scrolls    : is the current number of the opened scrolls
    def close_scroll_target(self, target, num_scrolls):
        times = 0   # times for the re-appearing object item
        # while the target scroll still exist.
        while num_scrolls == len(self.target_positions):
            # detects the object that is supposed to be the same number as the size
            # of the target position and right-click the x and y
            self.right_click_sroll(target[0], target[1])

    # Close up all the scrolls that was opened, popping out the elements from the
    # target positions list
    def close_scrolls(self):

        # while the target position size is not yet 0
        while len(self.target_positions) < 0:
            # closing the last position in the targeted position list
            # the water scroll will be closed until the last stage
            # then will pop out the target getting the new last position
            self.close_scroll_target(self.target_positions[-1],
                                     len(target_positions))
            # pops out the target position
            self.target_positions.pop()

    # ------------------------------------------------------------------------------
    # THIS PART WILL BE SUBJECTED FOR AN UPDATE ON A LATER DEVELOPMENT
    # ------------------------------------------------------------------------------

    # This method reads the following instructions -> the file must exist
    # if instructions.txt  doesn't exist, this will return error and program
    # must restart
    def read_instructions(self):
        # reading the text file
        file = open("instructions.txt", "r")
        # reading the file line by line
        for line in file:
            stripped = line.strip().split()
            # appending the stripped line by line values
            self.instructions.append(stripped)

    # What this method does is, there will be a instruction that is generated by the user
    # this instruction will exist in the file that the javaFX is going to create -> instruction.txt
    # this method will read the instruction and will process the instruction step by step
    # since MMORPG has different type of deleting or removing items from the inventory
    # this also contains all the x,y axis of the detected object
    def process_the_instruction(self):
        # For Debugging purposes
        print("moving to the {} {}".format(self.x_target, self.y_target))
        print(pyautogui.position())

    # This method will make a character object moving until it detects a new monster
    # in the scene and target that monster, depending on the instruction given
    # by the user on how to kill a monster in the game
    def detect_mobs_movement(self):
        # this redetects the movement inside
        movement = detector.locate()

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # position = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.
    def get_screen_position(self, position):
        return (position[0] + self.offset_x, position[1] + self.offset_y)

    # # -----------------------------------------------------------------
    # # -------------------- THREADING METHODS --------------------------
    # # -----------------------------------------------------------------

    # The method that will start the threading
    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    # Method that will stop the function of the thread
    def stop(self):
        self.stopped = True

    # Method that runs all the functionality of the AppBot
    def run(self):

        # first is to initiate the target positions
        while not self.stopped:

            # If the status of the bot is currently INITIALISING state
            if self.status == AppBotStatus.INITIALISING:
                # Locking the current state of the thread
                self.lock.acquire()
                # Bot will update the status to detecting
                # (BUT RIGHT NOW IT'S GOING FOR PROCESSING FOR TESTING PURPOSES)
                self.status = AppBotStatus.PROCESSING
                # Once the status of the application bot is updated then lock will release
                self.lock.release()

            # If the status of the bot is currently in DETECTING state
            elif self.status == AppBotStatus.DETECTING:
                # Locking the detection
                self.lock.acquire()
                # detector locating objects from the targeted application
                self.detecting_new_location()
                # If the targeted positions contains a points of targets
                if self.target_positions:
                    # updates bot status to processing
                    self.status = AppBotStatus.PROCESSING
                    # release the lock status
                    self.lock.release()

            # If the status of the bot is in SEARCH mode
            elif self.status == AppBotStatus.SEARCHING:
                # locking the status
                self.lock.acquire()
                # detecting the mob movement
                detected = self.detect_mobs_movement()
                # if there's a detected object
                if detected:
                    self.status = AppBotStatus.PROCESSING
                    # releasing the lock
                    self.lock.release()

            # If the status of the bot is currently in PROCESSING state
            elif self.status == AppBotStatus.PROCESSING:
                # locking up the status until all the processes are done
                self.lock.acquire()

                # current repeat
                curr_reps = 0
                if self.repeatition != curr_reps:
                    # open up the scrolls
                    self.open_scrolls()
                    # close the opened scrolls
                    self.close_scrolls()
                    # increments the current repeatition time
                    curr_reps = curr_reps + 1

                elif self.repeatition == curr_reps:
                    # reset the target positions
                    self.target_positions = []
                    # unlocking the status
                    self.lock.release()





