# Import the libraries

# TKinter is the GUI library
from tkinter import *
import tkinter.font as font
# cv2 is used for image processing and video streaming
import cv2
# os library is used to retrieve file paths for any os
# Thus making the the program executable on all PC platforms
import os
from detect import detection

logo_term = os.path.join(os.getcwd(), 'icon.ico')
logo_vs = os.path.join(os.path.join(os.getcwd(), 'venv'), 'icon.ico')

# Screen Calibration

def screenCal():

    # Base Directory of project
    base = os.path.dirname(os.path.abspath(__file__))
    # Cascade files of Directory
    haar = os.path.join(base, 'haar cascade files')
    # Bitmap Logo

    # Face Cascade file
    face = cv2.CascadeClassifier(os.path.join(haar, 'haarcascade_frontalface_alt.xml'))

    # Video Streaming
    cap = cv2.VideoCapture(1)

    while True:
        # Retrieves one frame of the video stream as a object
        ret, frame = cap.read()

        # Converts frame to grayscale for Image Processing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Applies pretrained face cascade model on grayscale frame
        faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))

        # Draws a rectangle around face
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y) , (x+w,y+h) , (100,100,100) , 1 )

        # Displays frame and the 'q' key is used to exit stream
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Ends video stream. This needs to be done to avoid memory issues
    cap.release()
    cv2.destroyAllWindows()

def activePage():

    # Hides previous window
    root.withdraw()

    # Child of root window
    active = Toplevel(root) 
  
    active.title("Impunity") 
    try:
        active.iconbitmap(logo_vs)
    except:
        print("Wrong Directory!")
        active.iconbitmap(logo_term)
    else:
        active.iconbitmap(logo_vs)
  
    # Size of window
    active.geometry("640x360")

    # Executes the drowsiness detection model
    detection()

    # Label and Button
    Label(active, text ="The Drowsiness Detector is active", font = hdFont).pack()
    Button(active, text = "Stop", height=2, width=10).place(relx=0.5, rely=0.5, anchor=CENTER)

def calPage():

    # Hides previous window
    root.withdraw()

    # Child of root window
    calibration = Toplevel(root) 
  
    calibration.title("Impunity") 
    try:
        calibration.iconbitmap(logo_vs)
    except:
        print("Wrong Directory!")
        calibration.iconbitmap(logo_term)
    else:
        calibration.iconbitmap(logo_vs)
  
    # Size of window
    calibration.geometry("640x360")
  
    # Labels and Buttons
    Label(calibration, text ="Screen Calibration", font = hdFont).pack() 
    Label(calibration, text="Place the camera on a surface where the camera points to your face").pack()
    Label(calibration, text="Press Start to begin calibration").pack()
    Label(calibration, text="When a rectangle appears around your face, press 'q' to end calibration").pack()
    Button(calibration, text="Start", command=screenCal, height=3, width=10).place(relx=0.5, rely=0.5, anchor=CENTER)
    Button(calibration, text="Next", command=activePage,height=2, width=10).place(relx=0.9, rely=0.9, anchor=SE)

# Window settings
root = Tk()
root.title('Impunity')
root.geometry('640x360')
try:
    root.iconbitmap(logo_vs)
except:
    print("Wrong Directory!")
    root.iconbitmap(logo_term)
else:
    root.iconbitmap(logo_vs)

# Font settings
hdFont = font.Font(family='Helvetica', size=30, weight='bold')
pFont = font.Font(family='Helvetica', size=10)

# Labels and Buttons
Label(root, text='Impunity', font=hdFont).place(relx=0.5, rely=0.45, anchor=S)
Label(root, text='Making your trip safer', font = pFont).place(relx=0.5, rely=0.5, anchor=CENTER)

btnNext = Button(root, text='Next', height=3, width=10, command = calPage)
btnNext.place(relx=0.5, rely=0.56, anchor=N)

# Similar to a Game Loop to keep the application running
root.mainloop()