import cv2 as cv
import numpy as np
from threading import Thread, Lock
"""
    Name:           Detector Class
    Information:    This class has a function of detecting the object inside a
                    Window Capture class, this provides the results of the points
                    and locate and draw the boxes that shows up that the targeted
                    object has matched an object inside the window capture
    Author:         Raphael Di Ezmo                                                     """

class Detector:

    # Detector properties
    target_object   = None  # Variable to hold the targeted image
    img_width       = 0     # image width of the image
    img_height      = 0     # image height of the image
    method_use      = None  # Method that is going to be used for matching
    win_capture     = None  # Window capture

    # # Threading properties
    # stop            = False # Holds the current status of the thread; stop = false => running
    # lock            = None  # Holds  the thread lock object


    # Constructor
    def __init__(self, target_object_path, method=cv.TM_CCOEFF_NORMED):
        # # Initializing the thread lock object
        # self.lock = Lock()

        # Fetching the targeted image that is subjected for detection
        # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
        self.target_object = cv.imread(target_object_path, cv.IMREAD_UNCHANGED)

         # Fetching the dimensions of the target object image
        self.img_width   = self.target_object.shape[1]
        self.img_height  = self.target_object.shape[0]

        # Some methods to pick from for testing, some of them might be more accurate
        # but it always depends on the scenario
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method_use = method

    # This function produces the detected object from the window capture class
    # Parameters:
    #       self            - this is a method of a class (mandatory parameter)
    #       window_capture  - the view of the cloned window of the targeted application
    #       threshold       - the percentage of matching targeted object detected
    #       debug_mode      - this proves that the object is detected by drawing rectangles
    def locate(self, window_capture, threshold=0.5):

        # getting the result matches from the window capture containing the targeted object image
        result = cv.matchTemplate(window_capture, self.target_object, self.method_use)

        # Getting all the position from the match result that meets
        # the criteria of the given threshold
        locs = np.where(result >= threshold)
        locs = list(zip(*locs[::-1]))
        #print(locs)

        # There will be overlapping rectangles when detecting the target object on the
        # window capture therefore to overcome the overlapping results this loop will
        # use groupRectangles() method
        rectangles = []
        for loc in locs:
            rect = [int(loc[0]), int(loc[1]), self.img_width, self.img_height]
            # Adding every box to the list 2x to retain
            rectangles.append(rect)
            rectangles.append(rect)

        # Grouping up the rectangles
        # The groupThreshold parameter, normally has a value of 1.
        # If = 0 then there will be no grouping. If 3 or more then object needs
        # to be a overlapping more than 2x therefore depending on the value you put,
        # you must multiply the number of adding the boxes to retain some of the
        # non-overlapping boxes exist on the screen detection.
        # eps - relative difference between sides of the rect to merge into the group
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        # Empty array that will hold all the points of the targeted
        # objects that matches the criteria
        points = []
        if len(rectangles):
            #print('Found an object')
            line_color      = (255, 20, 250)
            line_type       = cv.LINE_4
            marker_color    = (255,0,255)
            marker_type     = cv.MARKER_CROSS
#
            # Looping to all the rectangle inside the rectangles array
            for (x,y,w,h) in rectangles:

                # Getting the center points of the rectangles
                center_x = x + int(w/2)
                center_y = y + int(h/2)

                # Saving the points of the center's x and y axis
                points.append((center_x, center_y))

                # Getting the boxes in position
                top_l       = (x,y)         # Top left
                bottom_r    = (x+w, y+h)    # Bottom right

                # Drawing the rectangles on the targeted object
                cv.rectangle(window_capture, top_l, bottom_r, color=line_color,
                            lineType=line_type, thickness=2)


            # This is just for debugging purposes, normally the app won't show this
            # Just the targeted window
            cv.imshow('Window capture', window_capture)
            print("DETECTED {}".format(len(points)))

            # Returns the points, this could be use in the later part's development
            return points

    # # Method that will start the threading
    # def start(self):
    #     self.stopped = False
    #     t = Thread(target=self.run)
    #     t.start()
    #
    # # Method that will stop the function of the thread
    # def stop(self):
    #     self.stopped = True
    #
    # # Method that runs all the functionality of the AppBot
    # def run(self):
    #     while not self.stopped:






