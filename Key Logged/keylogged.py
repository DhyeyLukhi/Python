import keyboard
import pyautogui
import time
import pynput


def recordKeys():
    event = keyboard.record('enter')
    with open('.keys.txt', 'w') as file:
        for e in event:
            if e.event_type == 'down':
                file.write(f"'{e.name}'")
    

if __name__ == "__main__":
    print("Hello user...")
    print("I want to record some keys from your keyboard")
    recordKeys()

    






# if i have to write soemthing on the user console then use the pyautogui.write function instead of keyboard.write (use keyboard.wrte to get a feel like chatgpt is writing in the console)