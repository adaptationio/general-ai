import numpy as np
import random
from sklearn import preprocessing
import csv
import torch
import time
import cv2
import mss
import numpy
import pyautogui


class DataGrabber():
    """gets data and processes ready to use"""

    def __init__(self):
        
        self.love = 14


    def toarray(self, x):
        x = np.array(x, dtype=np.float32)
        return x


    def get_screen(self):
        with mss.mss() as sct:
            # Part of the screen to capture
            monitor = {"top": 40, "left": 0, "width": 800, "height": 640}

            while "Screen capturing":
                last_time = time.time()

                # Get raw pixels from the screen, save it to a Numpy array
                img = numpy.array(sct.grab(monitor))

                # Display the picture
                cv2.imshow("OpenCV/Numpy normal", img)

                # Display the picture in grayscale
                # cv2.imshow('OpenCV/Numpy grayscale',
                #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

                print("fps: {}".format(1 / (time.time() - last_time)))

                # Press "q" to quit
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break

    def get_screen_array(self, top, left, width, height):
        with mss.mss() as sct:
            monitor = {"top": top, "left": left, "width": width, "height": height}

            img = numpy.array(sct.grab(monitor))
            return img

    def get_screen_img_show(self, grey):
        with mss.mss() as sct:
            monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
            img = numpy.array(sct.grab(monitor))
            if grey == False:
                cv2.imshow("OpenCV/Numpy normal", img)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()

            else:
                cv2.imshow('OpenCV/Numpy grayscale', cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
            return img


class Controller():
    def __init__(self):
        
        self.love = 'Ramona'
        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 1 
    
    def actions(self, actions):
        action = actions[0]
        x = actions[1]
        y= actions[2]
        click = actions[3]
        self.action[self.move_mouse(x,y), self.click_mouse(click), self.move_click_mouse(x,y,click)]

    def yeah(self):
        cunt = "Cunt"

    def get_postiion(self):
        self.position = pyautogui.position()
        return self.position

    def get_screen_size(self):
        self.height, self.width = pyautogui.size()
        return self.height, self.width

    def move_mouse(self, x_coordinate, y_coordinate, duration):
        pyautogui.moveTo(x_coordinate, y_coordinate, duration)

    def click_mouse(self):
        pyautogui.click()

    def move_click_mouse(self, x, y, clicks, interval=1, button):
        pyautogui.click(x=x, y=y, clicks=clicks, interval=1, button='left')
    
    def key_press(self, key='enter'):
        pyautogui.press(key)


   

    

    
    

    

    
#dates = ["2016", "2017", "2018"]
test = DataGrabber()
test.get_screen()
#ata = test.load_state_2()
#print(len(data[1]))
#candles = test.get_candles(dates[0]+'-01-01T00:00:00Z', 2, "M1", "EUR_USD")
#some_data = test.data_converted(candles)
#some_data = test.toarray(some_data)
#some_data = test.normalize(some_data)
#some_data = test.totensor(some_data)
#data_day = some_data[0:1440]
#print(len(data_day))
#print(len(some_data))
#print(candles)
#print(some_data)
#test.get_screen()
#pyautogui.FAILSAFE = False
#pyautogui.PAUSE = 1 
#height,width = pyautogui.size()
#print(height)
#print(width)
#position = pyautogui.position()
#print(position)
#x_coordinate = 0
#y_coordinate = 0
#duration = 3
#pyautogui.moveTo(x_coordinate,y_coordinate,duration)
#pyautogui.moveTo(1000,1000,duration)
#pyautogui.click()



