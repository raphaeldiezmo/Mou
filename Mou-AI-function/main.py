import cv2 as cv
import numpy as np
from time import time
from pywin.framework.editor import color
from windowcapture import WindowCapture

"""
    Name:       Mou AI functionality
    Details:    This program will provide the Open CV functionality.
                This program will provide all the application window capture
                that will help the further functionality for object detection
    Author:     Raphael Di Ezmo
"""

# This application name will be only for Testing
app_name = 'Supreme Destiny            '

# Function that will get the window's application capturing the image content of a window
# this will produce the clone image and actions that has been done in the targeted
# application
# Parameters:
#       app_name this contains the window title of an application




# For testing purposes only
def test_object_image_detection():

    # Variables that holds the image
    y = cv.imread('y.JPG', cv.IMREAD_UNCHANGED)
    x = cv.imread('x.JPG', cv.IMREAD_UNCHANGED)

    # Result variable that will hold the percentage of the matching result
    result = cv.matchTemplate(y, x, cv.TM_CCOEFF_NORMED)

    # Getting the best match position
    # minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)


    # print('best match: %s' % str(maxLoc))
    # print('Best match confidence: %s percent' % int(maxVal*100))

    threshold = 0.55
    # Gets ONLY 1 result and will give the highest percentage of having a match
    # if maxVal >= threshold:
    #     print("Found the baldr weapon")
    #
    #     w = x.shape[1]
    #     h = x.shape[0]
    #
    #     top_left = maxLoc
    #     bot_right = (top_left[0] + w, top_left[1] + h)
    #
    #     cv.rectangle(y, top_left, bot_right,
    #                  color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    # cv.imshow('Result', y)
    # cv.waitKey()

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    print(locations)





def run_ai(app_name):

    # initialize the WindowCapture class
    wincap = WindowCapture(app_name)

    # time variable that will update the time inside the while loop
    time_updtr = time()



    # Runs the infinite loop until the user wants to end it
    while(True):

        # get an updated image of the game
        screen_detector = wincap.capture_window()

        # pops up a cloned window of the targeted application
        cv.imshow('Mou Window Capturer', screen_detector)

        # debug the loop rate
        print('FPS {}'.format(int(1 / (time() - time_updtr))))

        # updates the time
        time_updtr = time()

        # press '#' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('#'):
            cv.destroyAllWindows()
            break


#run_ai(app_name)
test_object_image_detection()
print('Execution done, all CV executed object has been successfully removed.')
