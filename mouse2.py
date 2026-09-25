from pynput import keyboard
from pynput.mouse import Controller
import time

# Mouse controller
mouse = Controller()

# Number of scroll "steps" whenever A is pressed
SCROLL_AMOUNT = -3


def on_press(key):
    try:
        # Whenever the A key is pressed
        if key.char.lower() == 'a':
            mouse.scroll(0, SCROLL_AMOUNT)
            print("A pressed -> scrolled down")

    except AttributeError:
        # Ignore special keys such as Shift, Ctrl, etc.
        pass


# ---------------------------------------------------------
# OPTIONAL MOUSE-CLICK MODE
# ---------------------------------------------------------
# Uncomment this section if you want:
#
#   Left click -> start scrolling continuously
#   Q          -> stop scrolling
#   Q again    -> continue scrolling
#
# ---------------------------------------------------------

# scrolling = False
#
# def on_click(x, y, button, pressed):
#     global scrolling
#
#     if button == Button.left and pressed:
#         scrolling = True
#
#
# def scroll_loop():
#     global scrolling
#
#     while True:
#         if scrolling:
#             mouse.scroll(0, -1)
#         time.sleep(0.05)
#
#
# def on_press(key):
#     global scrolling
#
#     try:
#         if key.char.lower() == 'q':
#             scrolling = not scrolling
#             print("Scrolling:", scrolling)
#
#     except AttributeError:
#         pass


# Start monitoring the keyboard
print("Keyboard monitor started.")
print("Press A to scroll down.")
print("Press Ctrl+C in the terminal to stop.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()