import keyboard
import pyautogui
import time
import pynput
import threading

def recordKeys():
    while True:
        event = keyboard.record('enter')
        with open('.keys.txt', 'w') as file:
            for e in event:
                if e.event_type == 'down':
                    file.write(f"'{e.name}'")


def mouseMonitor():
    while True:
        position = pyautogui.position()
        size = pyautogui.size()
        print(f"Click on X:{position.x}   Y:{position.y}    Size: Width:{size.width}  Height{size.height}")
        time.sleep(1)



if __name__ == "__main__":
    print("Hello user...")
    print("I want to record some keys from your keyboard")
    keyboardThread = threading.Thread(target=recordKeys)
    mouseThread = threading.Thread(target=mouseMonitor)

    keyboardThread.start()
    mouseThread.start()
    keyboardThread.join()
    mouseThread.join()    






# if i have to write soemthing on the user console then use the pyautogui.write function instead of keyboard.write (use keyboard.wrte to get a feel like chatgpt is writing in the console)