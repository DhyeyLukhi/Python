import tkinter
import cv2
import PIL.Image
import PIL.ImageTk
from functools import partial
import threading
import imutils
import time


# Global Variables
set_width = 640
set_height = 400

stream = cv2.VideoCapture("../ProTraining/clip1.mp4")


def videoplay(speed):
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=set_width, height=set_height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    canvas.create_text(125, 25, fill="Blue", font="Time 12 bold", text="DECISION PENDING")


def decision(result):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("decision.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=set_width, height=set_height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # wait for Some time
    time.sleep(2)

    # Show The Sponsor
    frame = cv2.cvtColor(cv2.imread("Sponser.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=set_width, height=set_height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # Wait for Some Seconds
    time.sleep(3)

    # Here is the decision
    if result == 'out':
        frame = cv2.cvtColor(cv2.imread("out.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=set_width, height=set_height)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    elif result == 'not out':
        frame = cv2.cvtColor(cv2.imread("not out.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=set_width, height=set_height)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=decision, args=("out",))
    thread.daemon = 1
    thread.start()
    print("You Give OUT")


def notout():
    thread = threading.Thread(target=decision, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("You Give NOT OUT")


window = tkinter.Tk()
window.title("The DRS")
cv_img = cv2.cvtColor(cv2.imread("decision.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=set_width, height=set_height)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

# Buttons for Control
previousfast = tkinter.Button(window, text="<<  PREVIOUS(FAST) ", width=50, command=partial(videoplay, -10))
previousfast.pack()
previousslow = tkinter.Button(window, text="<<  PREVIOUS(SLOW) ", width=50, command=partial(videoplay, -2))
previousslow.pack()
nextslow = tkinter.Button(window, text="  NEXT(SLOW)  >>", width=50, command=partial(videoplay, 2))
nextslow.pack()
nextfast = tkinter.Button(window, text="  NEXT(FAST)  >>", width=50, command=partial(videoplay, 10))
nextfast.pack()
giveout = tkinter.Button(window, text="<<   GIVE OUT   >>", width=50, command=out)
giveout.pack()
givenotout = tkinter.Button(window, text="<<   GIVE NOT OUT   >>", width=50, command=notout)
givenotout.pack()


window.mainloop()
