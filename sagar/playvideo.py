# importing libraries 
import cv2
import numpy as np
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file


# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture(filename)

# Check if camera opened successfully 
if (cap.isOpened() == False):
    print("Error opening video file")

# Read until video is completed 
while (cap.isOpened()):

# Capture frame-by-frame 
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
