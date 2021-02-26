from tkinter import *
import cv2
import numpy as np
import sys
import os

class GUI(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()


        def buttonClick():
            os.system('python recordvideo.py')
           
            
        self.submitButton = Button(master, text="Record A Video", command=buttonClick)
        self.submitButton.grid()
        def buttonClick1():
            os.system('python playvideo.py')
           
            
        self.submitButton = Button(master, text="Play A Video", command=buttonClick1)
        self.submitButton.grid()

if __name__ == "__main__":
    guiFrame = GUI()    
    guiFrame.mainloop()
