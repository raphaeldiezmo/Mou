import numpy as np
import win32gui, win32ui, win32con
from threading import Thread, Lock
"""
    Name:           Window Capture Class
    Information:    This class provides the functionality of capturing the window
                    of the targeted application.
    Author:         Raphael Di Ezmo                                             """

class WindowCapture:

    # Window Capture properties
    hwnd        = None  # Handler of the targeted application's window
    width       = 0     # Holds the width of the window of the targeted application window
    height      = 0     # Holds the height of the window of the targeted app window
    cropped_x   = 0     # Holds the border pixels (x axis)
    cropped_y   = 0     # Holds the border pixels (y axis)
    offset_x    = 0     # Helper for centering the window capture's content
    offset_y    = 0     # Helper for centering the window capture's content

    # # Threading properties
    # stop        = True  # Thread's current state True = stops the thread
    # lock        = None  # Locks up the current thread's state
    # wincap      = None  # window capture for updating the window capture in the thread

    # Constructor
    # Parameter: window_name this holds up the window title name of an application
    def __init__(self, window_name=None):
        # initialising thread lock object
        self.lock = Lock()
        # Finding the handler of the window that is going to be captured
        # If the window name is not specified, it will capture the entire screen
        if window_name is None:
            self.hwnd = win32gui.getDesktopWindow()

        # Otherwise it will capture the specific window
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            # If the window name doesn't exist exception
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))

        # Getting the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.width = window_rect[2] - window_rect[0]
        self.height = window_rect[3] - window_rect[1]

        # Taking out the massive borders and the empty parts of the window capture
        border_pixels = 8
        title_bar_pixels = 30
        self.width = self.width - (border_pixels * 2)
        self.height = self.height - title_bar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = title_bar_pixels

        # Setting the cropped coordinates offset for better capture
        # and getting the proper position on the window output
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y


    # This function holds the captured window
    # produces the same image as the targeted function
    def capture_window(self):

        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.width, self.height)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.width, self.height), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.height, self.width, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type() 
        #   && _img.dims() <= 2 in function 'cv::matchTemplate'
        img = img[...,:3]

        # make image C_CONTIGUOUS to avoid errors that look like:
        #   File ... in draw_rectangles
        #   TypeError: an integer is required (got type tuple)
        # see the discussion here:
        # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        img = np.ascontiguousarray(img)

        return img

    # For testing purpose, prints all the possible window names that currently
    # running on the system
    # https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    def list_window_names(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # position = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.
    def get_screen_position(self, position):
        return (position[0] + self.offset_x, position[1] + self.offset_y)

    #
    # # -----------------------------------------------------------------
    # # -------------------- THREADING METHODS --------------------------
    # # -----------------------------------------------------------------
    # # This method initializes the thread and start the thread
    # def start(self):
    #     # Re-initializing the stop variable
    #     self.stop = False
    #     # Initializing the thread holding the run method
    #     thread = Thread(target=self.run)
    #     # Starts up the thread
    #     thread.start()
    # # Method to stop the thread of the class
    # def stop(self):
    #     # Changes up the value and make the thread stop
    #     self.stop = True
    # # Method to run the thread until the stop method is called to stop
    # def run(self):
    #     while not self.stop:
    #         # Locking the thread while updating the capture
    #         self.lock.acquire()
    #         # getting the update image of the window application
    #         self.capture_window()
    #         self.lock.release()
