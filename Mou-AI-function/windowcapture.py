import numpy as np
import win32gui, win32ui, win32con
"""
    Name:       Window Capture Class
    Details:    This class provides the functionality of capturing the window
                of the targeted application.
    Author:     Raphael Di Ezmo
"""

class WindowCapture:

    # Window Capture properties
    w           = 0     # Holds the width of the window of the targeted application window
    h           = 0     # Holds the height of the window of the targeted app window
    hwnd        = None  # Handler of the targeted app window
    cropped_x   = 0     # Holds the border pixels (x axis)
    cropped_y   = 0     # Holds the border pixels (y axis)
    offset_x    = 0     # Helper for centering the window capturer's content
    offset_y    = 0     # Helper for centering the window capturer's content

    # Constructor
    def __init__(self, window_name):

        # Finding the handler of the window that is going to be captured
        self.hwnd = win32gui.FindWindow(None, window_name)
        # If the window name doesn't exist exception
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))

        # Getting the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # Taking out the massive borders and the empty parts of the window capturer
        border_pixels = 8
        title_bar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - title_bar_pixels - border_pixels
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
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

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
    # pos = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.
    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)
