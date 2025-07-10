import webbrowser
import os
import keyboard


print("C: ChatGPT")
print("Y: YouTube")
print("D: YouTube/Dowbloads")
print("T: Telegram")


while True:
    key = keyboard.read_event(suppress=True)
    if key.event_type == keyboard.KEY_DOWN:
        if key.name == 'c' or key.name == 'C':
            webbrowser.open("https://chatgpt.com/")

        elif key.name == 'y' or key.name == 'Y':
            webbrowser.open("https://www.youtube.com")

        elif key.name == 'd' or key.name == 'D':
            webbrowser.open("https://www.youtube.com/feed/downloads")

        elif key.name == 't' or key.name == 'T':
            os.startfile("C:\\Users\\admin\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")

        elif key.name == 'enter':
            break
