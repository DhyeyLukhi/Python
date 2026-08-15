from pynput.mouse import Button, Controller
from pynput.keyboard import Listener

import threading
import time

mouse = Controller()

clicking = True
running = True


def click_loop():
    global clicking

    while running:
        if clicking:
            mouse.click(Button.left)
            time.sleep(0.01)  # 20 clicks per second
        else:
            time.sleep(0.01)


def on_press(key):
    global clicking

    try:
        if key.char.lower() in ("p", "q"):
            clicking = not clicking

            if clicking:
                print("▶ Clicking RESUMED")
            else:
                print("⏸ Clicking PAUSED")

    except AttributeError:
        pass


print("Auto-clicker started.")
print("Press P or Q to pause/resume.")
print("Press Ctrl+C in the terminal to exit.")

click_thread = threading.Thread(target=click_loop, daemon=True)
click_thread.start()

try:
    with Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    running = False
    print("\nAuto-clicker stopped.")