import os
import re
import shutil
import pyttsx3
import webbrowser as web
import datetime
import subprocess
import psutil


def search(path, item):
    i = 0
    for root, dirs, files in os.walk(path):
        if item in dirs or item in files:
            print(f"Your '{item}' is Founded at : {os.path.join(root, item)}\n")
            return 0
    return 1


def say(text):  # say: This function will speak
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return text


def explore_folders(path):
    # Iterate over all the items in the given path
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            print(item_path)  # Print the folder path

            explore_folders(item_path)
    return 0


def make_folder(path):  # When you are in the diks
    name = input("Enter the name: ")
    try:
        if "\\" in name.lower() or "/" in name.lower() or "<" in name.lower() or ">" in name.lower() or ":" in name.lower() or "*" in name.lower() or "?" in name.lower() or "|" in name.lower() or "'" in name.lower():
            print(r"Name cannot contain '\', '/', '<', '>', ':', '*', '|', '?', '' ")
            say("That's not possible")
            print(r"Name cannot contain \\, /, <, >, :, *, ?, |, ''")
            say("That's not possible")

        else:
            folder_path = os.path.join(path, name)
            os.mkdir(folder_path)
            print("Fodler Created Successfuly")
            say("Folder Create, Sir")
            return 0

    except Exception as e:
        print("There is an ERROR coming to create a folder")
        say("There is an ERROR for Folder")
        return 1


def multiple_folder(path):  # When you are in the diks
    number = int(input("Enter the number of folders: "))
    for i in range(0, number):
        name = input(f"Name of {i+1} Folder: ")

        if "\\" in name.lower() or "/" in name.lower() or "<" in name.lower() or ">" in name.lower() or ":" in name.lower() or "*" in name.lower() or "?" in name.lower() or "|" in name.lower() or "'" in name.lower():
            print(r"Name cannot contain '\', '/', '<', '>', ':', '*', '|', '?', '' ")
            say("That's not possible")
            print(r"Name cannot contain \\, /, <, >, :, *, ?, |, ''")
            say("That's not possible")

        else:
            try:
                folder_path = os.path.join(path, name)
                os.mkdir(folder_path)
                print("Fodler Created Successfuly")
                return 0

            except Exception as e:
                print("There is an ERROR coming to create a folder")
                say("There is an ERROR for Folder")
                return 1

        if i == number - 1:
            say("Folders are Created Successfully, sir")


def delete_folder(path):  # When you are in the diks
    try:
        name = input("Enter the name: ")
        folder_path = os.path.join(path, name)
        shutil.rmtree(folder_path)
        print("Folder Deleted Successfuly")
        say("Folder Deleted, Sir")
        return 0

    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR for this")
        return 1


def del_multi_folder(path):  # When you are in the diks
    try:
        number = int(input("Enter the number of Fodlers: "))
        for i in range(0, number):
            name = input(f"Name of {i+1} Folder: ")
            folder_path = os.path.join(path, name)
            shutil.rmtree(folder_path)
            print("Folder Deleted Successfuly")

            if i == number - 1:
                say("Folders are Deleted Successfuly, sir")
                return 0

    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR for this")
        return 1


def make_file(path):  # When you are in the diks
    try:
        name = input("Name of file(without extension): ")
        if "\\" in name.lower() or "/" in name.lower() or "<" in name.lower() or ">" in name.lower() or ":" in name.lower() or "*" in name.lower() or "?" in name.lower() or "|" in name.lower() or "'" in name.lower():
            print(r"Name cannot contain '\', '/', '<', '>', ':', '*', '|', '?', '' ")
            say("That's not possible")

        else:
            exte = input("Extension: ")
            name += exte
            file_path = os.path.join(path, name)
            with open(file_path, "w") as file:
                pass
            print("File Created Successfuly")
            say("File Created, Sir")
            return 0

    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR for this")
    return 1


def multi_file(path):  # When you are in the diks
    try:
        number = int(input("Enter the number: "))
        for i in range(0, number):
            name = input(f"Name of {i+1} File(without extension): ")
            if "\\" in name.lower() or "/" in name.lower() or "<" in name.lower() or ">" in name.lower() or ":" in name.lower() or "*" in name.lower() or "?" in name.lower() or "|" in name.lower() or "'" in name.lower():
                print(r"Name cannot contain '\', '/', '<', '>', ':', '*', '|', '?', '' ")
                say("That's not possible")

            else:
                exte = input("Extension : ")
                name += exte
                file_path = os.path.join(path, name)
                with open(file_path, "w") as file:
                    pass
                print("File Created Successfuly")

            if i == number - 1:
                say("Files are Created Successfully, sir")
                return 0

    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR for this")
    return 0


def delete_file(path):  # When you are in the diks
    try:
        name = input(f"Name of File(without extension): ")
        exte = input("Extension : ")
        name += exte
        file_path = os.path.join(path, name)
        os.remove(file_path)
        print("File Deleted Successfuly")
        say("File Deleted, Sir")
    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR to do this")
    return 1


def del_multi_file(path):  # When you are in the diks
    try:
        number = int(input("Enter the Numbers: "))
        for i in range(0, number):
            name = input(f"Name of {i+1} File(without extension): ")
            exte = input("Extension: ")
            name += exte
            file_path = os.path.join(path, name)
            os.remove(file_path)
            print("File Deleted Successfuly")
            if i == number - 1:
                say("Files are Deleted Successfully, sir")
    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR to do this")
        return 1


def get_items(directory):  # Get the list of all The items available in the directory
    items = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        items.append(item)
    return items


def wish():  # wish: This function wish user
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        say("Good Morning Sir, I am TIVIS")
    elif 12 <= hour < 18:
        say("Good Afternoon Sir, I am TIVIS")
    else:
        say("Good Evening Sir, I am TIVIS")


def assist():  # assist: Ready for your command
    print("TIVIS is here for your Assist, Sir")
    print("TIVIS is now going to smart for You")
    print("TIVIS - Version 10i")
    print("Type 'list of commands in assistant' to get all the exectuable commands.")
    say("TIVIS is here for your Assist, Sir")


def take_command():  # This function will take command form user
    user_command = str(input("Command: "))
    return user_command


def rename(path):
    items = get_items(path)
    oldname = input("Enter existing name: ")
    oldnamepath = os.path.join(path, oldname)
    j = 0
    for item in items:

        if oldname == items[j]:
            print("Item Founded")
            newname = input("Enter new name: ")
            newnamepath = os.path.join(path, newname)
            try:
                os.rename(oldnamepath, newnamepath)
                print("Rename Successfull")
                break
            except Exception as e:
                print("RENAME Unsuccessful")
                break

        elif oldname != items[j]:
            j += 1


def move(path1):
    items = get_items(path1)
    name = input("Enter the name: ")
    j = 0
    for j in range(0, len(items)):

        if name == items[j]:
            print("File Founded")
            oldpath = os.path.join(path1, name)
            newpath = input(r"Enter the place(e.g. C:\\User\\yourfolder\\): ")
            newpath = os.path.join(path1, newpath)

            try:
                shutil.move(oldpath, newpath)
                print("File Moved Successfull")
                break

            except Exception as e:
                print("File Moving Unsuccessful")
                break


def copyfile(path1):
    items = get_items(path1)
    name = input("Enter the name: ")
    j = 0
    for j in range(0, len(items)):
        if name == items[j]:
            paths = path1 + name
            paths = os.path.join(path1, name)
            print("File Copied Succesfully")
            destpath = input(r"Enter the destination(e.g. C:\\User\\Yourfolder\\): ")
            try:
                shutil.copy(paths, destpath)
                print("File Transfer Successful")
                break
            except Exception as e:
                print("File Transer Failed")
                say("File Transer is Failed")
                break


def copyfolder(path):
    items = os.listdir(path)
    name = input("Enter the name of the folder: ")
    j = 0
    for j in range(0, len(items)):
        if name == items[j]:
            path1 = os.path.join(path, name)
            print("Folder Founded")
            destpath = input(r"Enter the Destinantion(e.g. C:\\User\\Your Folder\\): ")
            try:
                shutil.copytree(path1, os.path.join(destpath, name))
                print("Folder Transferd to Destination")
                break
            except Exception as e:
                print("Copy or Transfer of the folder is Failed")
                say("There is an Error for this")
                break


def website(number):
    websites = ["https://www.youtube.com", "https://www.google.com", "https://www.wikipedia.org", "https://chat.openai.com", "https://web.whatsapp.com/", "https://web.telegram.org/k/"]
    sitename = ["YouTube", "Google", "Wikipedia", "ChatGPT", "Whatsapp", "Telegram"]
    web.open_new_tab(websites[number])
    print("Executing...")
    say(f"Opening {sitename[number]}, sir")

    return 0


if __name__ == "__main__":
    wish()
    assist()
    print("Ready to execute your command")

    while True:
        # Taking Command from User
        command = take_command()

        try:
            # Open YouTube by using Chrome
            if "open youtube" in command.lower():  # Open youtube
                website(0)

            # Open Google by using Chorme
            if "open google" in command.lower():  # Open google
                website(1)

            # Open Wikipedia by using Chorme
            if "open wikipedia" in command.lower():  # Open wikipedia
                website(2)

            # Time Getting Function
            if "what is the time now" in command.lower() or "time now" in command.lower():  # Telling the time
                print(f"{datetime.datetime.now().strftime('%I : %M %p')}")
                hours, minutes = datetime.datetime.now().strftime("%I"), datetime.datetime.now().strftime("%M")
                if hours.startswith("0") and minutes.startswith("0"):
                    hours = hours[1:]
                    minutes = minutes[1:]
                    say(f"Time is {hours} hours and {minutes} minutes {datetime.datetime.now().strftime('%p')}")
                elif hours.startswith("0"):
                    hours = hours[1:]
                    say(f"Time is {hours} hours and {minutes} minutes {datetime.datetime.now().strftime('%p')}")
                elif minutes.startswith("0"):
                    minutes = minutes[1:]
                    say(f"Time is {hours} hours and {minutes} minutes {datetime.datetime.now().strftime('%p')}")
                else:
                    say(f"Time is {hours} hours and {minutes} minutes {datetime.datetime.now().strftime('%p')}")

            # Date Getting Function    # Date of today and now Day of week
            if ("date" in command.lower() and "today" in command.lower()) or ("day" in command.lower() and "today" in command.lower()) or ("day" in command.lower() and "week" in command.lower()):
                date = datetime.date.today()
                print(f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')}/{datetime.datetime.now().strftime('%G')}")
                print(f"Day : {datetime.datetime.now().strftime('%A')}")
                print(f"Month : {datetime.datetime.now().strftime('%B')}")
                say(f"Today's Date is {date}")
                say(f"Day is {datetime.datetime.now().strftime('%A')}")

            # Open ChatGPT in chrome
            if "open chatgpt" in command.lower():  # Open chatGPT
                website(3)

            # This is not for everyone
            if "open pycharm" in command.lower() or "open pc" in command.lower():  # Open PyCharm
                path = "C:\\Program Files\\Jetrains\\PyCharm Community Edition 2023.1.3\\bin\\pycharm64.exe"
                try:
                    if os.path.exists(path):
                        subprocess.Popen(path)
                        print("Executing...")
                        say("opening PyCharm, sir")
                except Exception as e:
                    pass

            # To open VS Code
            if "open vs code" in command.lower():
                path = "C:\\Users\\shubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                try:
                    if os.path.exists(path):
                        subprocess.Popen(path)
                        print("Executing...")
                        say("Opening VS code, Sir")

                except Exception as e:
                    pass

            # Open chorme
            if "open chrome" in command.lower():  # pen Chrome
                path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                try:
                    subprocess.Popen(path)
                    print("Executing...")
                    say("Opening Chrome, Sir")

                except Exception as e:
                    website(2)

            # Open Web-Whatsapp by using this
            if "open whatsapp" in command.lower():  # Open Whatsapp
                website(4)

            # Open web'Telegram by Using this
            if "open telegram" in command.lower():  # Open Telegram
                website(5)

            # Search something on YouTube is now Possible
            if "search" in command.lower() and "in youtube" in command.lower():
                start = "search"
                end = "in youtube"
                pattern = re.compile(f"{re.escape(start)}(.*?){re.escape(end)}")
                match = pattern.search(command)
                if match:
                    youtube_search = match.group(1).strip()
                    youtube_search = youtube_search.replace(" ", "+")
                    web.open(f"https://www.youtube.com/results?search_query={youtube_search}")

            # Do you want to search on Google? Don't worry this will do
            if "tell me about" in command.lower() and "yourself" not in command.lower() and "TIVIS" not in command.lower():
                match = re.search(r"tell me about (.+)", command, re.IGNORECASE)
                if match:
                    search = match.group(1).strip()
                    search = search.replace(" ", "+")
                    web.open(f"https://www.google.com/search?q={search}")

            # This can open any Drive you want inyour PC
            if "open" in command.lower() and "drive" in command.lower():
                drive = re.search(f"open (.+) drive", command.lower(), re.IGNORECASE)
                if drive:
                    path = drive.group(1).strip()
                    path.upper()
                    path = path + ":" + "\\"
                    items = get_items(path)
                    for i in range(0, len(items)):
                        print(f"{i+1}. {items[i]}")
                    while True:
                        enter = str(input("Enter the Command: "))
                        try:
                            if "<exit>" in enter.lower():
                                path = ""
                                break

                            elif "make" in enter.lower() and "folder" in enter.lower() and "multiple" not in enter.lower():
                                make_folder(path)

                            elif "make" in enter.lower() and "multiple" in enter.lower() and "folder" in enter.lower():
                                multiple_folder(path)

                            elif "delete" in enter.lower() and "folder" in enter.lower() and "multiple" not in enter.lower():
                                delete_folder(path)

                            elif "delete" in enter.lower() and "multiple" in enter.lower() and "folder" in enter.lower():
                                del_multi_folder(path)

                            elif "make" in enter.lower() and "file" in enter.lower() and "multiple" not in enter.lower():
                                make_file(path)

                            elif "make" in enter.lower() and "multiple" in enter.lower() and "file" in enter.lower():
                                multi_file(path)

                            elif "delete" in enter.lower() and "file" in enter.lower() and "multiple" not in enter.lower():
                                delete_file(path)

                            elif "delete" in enter.lower() and "multiple" in enter.lower() and "file" in enter.lower():
                                del_multi_file(path)

                            elif "rename" in enter.lower():
                                rename(path)

                            elif ("move" in enter.lower() and " file" in enter.lower()) or ("cut" in enter.lower() and " file" in enter.lower()) or ("move" in enter.lower() and " folder" in enter.lower()) or ("cut" in enter.lower() and " folder" in enter.lower()):
                                move(path)

                            elif "copy" in enter.lower() and "file" in enter.lower():
                                copyfile(path)

                            elif "copy" in enter.lower() and "folder" in enter.lower():
                                copyfolder(path)

                            elif "open youtube" in enter.lower():
                                website(0)

                            elif "open google" in enter.lower():
                                website(1)

                            elif "open wikipedia" in enter.lower():
                                website(2)

                            elif "open chatgpt" in enter.lower():
                                website(3)

                            elif "open whatsapp" in enter.lower():
                                website(4)

                            elif "open telegram" in enter.lower():
                                website(5)

                            elif "what is the time now" in enter.lower() or "time now" in enter.lower():  # Telling the time
                                print(f"{datetime.datetime.now().strftime('%I : %M %p')}")
                                hours, minutes = datetime.datetime.now().strftime("%I"), datetime.datetime.now().strftime("%M")
                                if hours.startswith("0") and minutes.startswith("0"):
                                    hours = hours[1:]
                                    minutes = minutes[1:]
                                    say(f"Time is {hours} hours and {minutes} minutes {datetime.datetime.now().strftime('%p')}")
                                elif hours.startswith("0"):
                                    hours = hours[1:]
                                    say(f"Time is {hours} hours and {minutes} minutes {datetime.datetime.now().strftime('%p')}")
                                elif minutes.startswith("0"):
                                    minutes = minutes[1:]
                                    say(f"Time is {hours} hours and {minutes} minutes {datetime.datetime.now().strftime('%p')}")
                                else:
                                    say(f"Time is {hours} hours and {minutes} minutes {datetime.datetime.now().strftime('%p')}")

                            elif ("date" in enter.lower() and "today" in enter.lower()) or ("day" in enter.lower() and "today" in enter.lower()) or ("day" in enter.lower() and "week" in enter.lower()):
                                date = datetime.date.today()
                                print(f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')}/{datetime.datetime.now().strftime('%G')}")
                                print(f"Day : {datetime.datetime.now().strftime('%A')}")
                                print(f"Month : {datetime.datetime.now().strftime('%B')}")
                                say(f"Today's Date is {date}")
                                say(f"Day is {datetime.datetime.now().strftime('%A')}")

                            elif "give" in enter.lower() and "list" in enter.lower():
                                items = get_items(path)
                                for i in range(0, len(items)):
                                    print(f"{i+1}. {items[i]}")

                            elif "open" in enter.lower() and "website" in enter.lower():
                                match = re.search(f"open (.*?) website", command, re.IGNORECASE)
                                if match:
                                    webname = match.group(1)
                                    web.open(f"https://www.{webname}")

                            # It is able to check the battery status
                            elif "battery" in enter.lower() and "status" in enter.lower():
                                try:
                                    battery = psutil.sensors_battery()

                                    if battery.power_plugged:
                                        if battery.percent == 100:
                                            print(f"Battery Status : Fully Charged : {battery.percent}%")
                                            say("Battery is Fully Charged")

                                        else:
                                            print(f"Battery Status : Charging : {battery.percent}%")
                                            say(f"Battery is {battery.percent}% and Charging ")

                                    else:
                                        if battery.percent == 100:
                                            print(f"Battery Status : Fully Charged : {battery.percent}%, Started Discharging")
                                            say("Battery is Fully Charged and started Discharging")

                                        else:
                                            print(f"Battery Status : Discharging : {battery.percent}%")
                                            say(f"Battery is {battery.percent}% left")

                                except Exception as e:
                                    print("I can't get the Value")
                                    say("I can't get this")

                            # It can do simple mathameticle calculations
                            elif ("/" in enter) or ("*" in enter) or ("+" in enter) or ("-" in enter):
                                try:
                                    result = eval(enter)
                                    print(f"Result : {result}")

                                except (SyntaxError, ZeroDivisionError):
                                    pass

                            # It can serch any item form your laptop
                            elif "search" in enter.lower() and "item" in enter.lower():
                                location = input("Drive: ")
                                itemname = input("Item: ")
                                if not location or not location.strip():
                                    if not itemname or not itemname.strip():
                                        print("Can't Find Your Item")
                                    else:
                                        for c in range(ord("A"), ord("Z")):
                                            location = chr(c) + ":\\"
                                            try:
                                                check = search(location, itemname)
                                                if check == 1 and chr(c) == "Z":
                                                    print("Can't Find Your Item")
                                                    break
                                                if check == 0:
                                                    break
                                            except Exception as e:
                                                pass

                                else:
                                    location = location.upper() + ":\\"
                                    check = search(location, itemname)
                                    if check == 1:
                                        print("Can't Find Your Item")
                                    if check == 0:
                                        pass

                            # Memory Usage of your Disk
                            elif "memory usage" in enter.lower():
                                way = input("Enter the Drive: ")
                                mem_drive = way.upper() + ":\\"

                                try:
                                    usage = psutil.disk_usage(mem_drive)
                                    print(f"Total  : {(usage.total / (1024 ** 3)):.2f} GB")
                                    print(f"Used   : {(usage.used / (1024 ** 3)):.2f} GB")
                                    print(f"Used(%) : {usage.percent :.2f} % ")
                                    print(f"Left   : {(usage.total / (1024 ** 3)) - (usage.used / (1024 ** 3)):.2f} GB ")
                                    print(f"Left(%) : {100 - usage.percent :.2f} % ")
                                    say(f"You have {(usage.total / (1024 ** 3)):.2f} GB Memory in {way} Drive")
                                    say(f"You have used {(usage.used / (1024 ** 3)):.2f} GB ")
                                    say(f"You have used {usage.percent :.2f} % ")

                                except Exception as e:
                                    way = ""
                                    print("Here is ERROR, Try again")
                                    say("I can't Find the memory usage at your provided Drive")

                            # Here us the list of all commands which are exectable
                            elif "list" in enter.lower() and "commands" in enter.lower() and "assistant" in enter.lower():
                                print(r"1. Open YouTube - To open YouTube using Google Chrome")
                                print(r"2. Open Google - To open Google using Google Chrome")
                                print(r"3. Open Chrome - To open Chrome either using Chrome.exe or using https://www.google.com")
                                print(r"4. Open ChatGPT - To open ChatGPT in Chrome")
                                print(r"5. Time now - To know the current Time")
                                print(r"6. Date Today - To know the Date of Today")
                                print(r"7. Open Wikipedia - To open Wikipedia using Chrome")
                                print(r"8. Open Whatsapp - To open Web-Whatsapp")
                                print(r"9. Open Telegram - To open Web-Telegram")
                                print(r"10. Open {{drive-character}} Drive - To open Desire drive in your PC")
                                print(r"11. Open {{websiten-name.TLD}} website - To open Desire Website")
                                print(r"12. Search {{your-search-in-YouTube}} in YouTube - To open Desire Searched page on YouTube")
                                print(r"13. Tell me about {{you-query}} - To Search your Query on Google")
                                print(r"14. Battery Percentage - To know Battery Status of your Laptop")
                                print(r"15. You can also use me as a standard Calculator by entering the problems.txt")
                                print(r"16. Search Item - To search any item in your PC or Laptop")
                                print(r"17. Memory Usage = To know the Memory Usage in your Drive")
                                say("Here is the list of Commands that I can Execute in this Version")

                            elif "search" in enter.lower() and "in youtube" in enter.lower:
                                start = "search"
                                end = "in youtube"
                                pattern = re.compile(f"{re.escape(start)}(.*?){re.escape(end)}")
                                match = pattern.search(enter)
                                if match:
                                    youtube_search = match.group(1).strip()
                                    youtube_search = youtube_search.replace(" ", "+")
                                    web.open(f"https://www.youtube.com/results?search_query={youtube_search}")

                            # Do you want to search on Google? Don't worry this will do
                            elif "tell me about" in enter.lower() and "yourself" not in enter.lower() and "tivis" not in enter.lower():
                                match2 = re.search(r"tell me about (.+)", enter, re.IGNORECASE)
                                if match2:
                                    search = match2.group(1).strip()
                                    search = search.replace(" ", "+")
                                    web.open(f"https://www.google.com/search?q={search}")

                            else:
                                name = re.search(r"open (.+)", enter, re.IGNORECASE)
                                newpath = name.group(1).strip()
                                if os.path.isdir(path + newpath + "\\"):

                                    try:
                                        path = path + newpath + "\\"
                                        items = get_items(path)
                                        for i in range(0, len(items)):
                                            print(f"{i + 1}. {items[i]}")
                                    except Exception as e:
                                        pass

                                if os.path.isfile(path + newpath):

                                    try:
                                        file = name.group(1)
                                        os.startfile(path + str(file))

                                    except Exception as e:
                                        pass

                        except Exception as e:
                            pass

            # This can open any website
            if "open" in command.lower() and "website" in command.lower():
                match = re.search(f"open (.*?) website", command, re.IGNORECASE)
                if match:
                    webname = match.group(1)
                    web.open(f"https://www.{webname}")

            # It is able to check the battery status
            if "battery" in command.lower() and "status" in command.lower():
                try:
                    battery = psutil.sensors_battery()

                    if battery.power_plugged:
                        if battery.percent == 100:
                            print(f"Battery Status : Fully Charged : {battery.percent}%")
                            say("Battery is Fully Charged")

                        else:
                            print(f"Battery Status : Charging : {battery.percent}%")
                            say(f"Battery is {battery.percent}% and Charging ")

                    else:
                        if battery.percent == 100:
                            print(f"Battery Status : Fully Charged : {battery.percent}%, Started Discharging")
                            say("Battery is Fully Charged and started Discharging")

                        else:
                            print(f"Battery Status : Discharging : {battery.percent}%")
                            say(f"Battery is {battery.percent}% left")

                except Exception as e:
                    print("I can't get the Value")
                    say("I can't get this")

            # It can do simple mathameticle calculations
            if "/" in command or "*" in command or "+" in command or "-" in command:
                try:
                    result = eval(command)
                    print(f"Result : {result}")

                except (SyntaxError, ZeroDivisionError, NameError, TypeError) as e:
                    pass

            # It can serch any item form your laptop
            if "search" in command.lower() and "item" in command.lower():
                location = input("Drive: ")
                itemname = input("Item: ")
                if not location or not location.strip():
                    if not itemname or not itemname.strip():
                        print("Can't Find Your Item")
                    else:
                        for c in range(ord("A"), ord("Z")):
                            location = chr(c) + ":\\"
                            try:
                                check = search(location, itemname)
                                if check == 1 and chr(c) == "Z":
                                    print("Can't Find Your Item")
                                    break
                                if check == 0:
                                    break
                            except Exception as e:
                                pass

                else:
                    location = location.upper() + ":\\"
                    check = search(location, itemname)
                    if check == 1:
                        print("Can't Find Your Item")
                    if check == 0:
                        pass

            # Memory Usage of your Disk
            if "memory usage" in command.lower() or 'memory status' in command.lower():
                way = input("Enter the Drive: ")
                mem_drive = way.upper() + ":\\"

                try:
                    usage = psutil.disk_usage(mem_drive)
                    print(f"Total   : {(usage.total / (1024 ** 3)):.2f} GB")
                    print(f"Used    : {(usage.used / (1024 ** 3)):.2f} GB")
                    print(f"Used(%) : {usage.percent :.2f} % ")
                    print(f"Left    : {(usage.total / (1024 ** 3)) - (usage.used / (1024 ** 3)):.2f} GB ")
                    print(f"Left(%) : {100 - usage.percent :.2f} % ")
                    say(f"You have {(usage.total / (1024 ** 3)):.2f} GB Memory in {way} Drive")
                    say(f"You have used {(usage.used / (1024 ** 3)):.2f} GB ")
                    say(f"You have used {usage.percent :.2f} % ")

                except Exception as e:
                    way = ""
                    print("Here is ERROR, Try again")
                    say("I can't Find the memory usage at your provided Drive")

            # Here us the list of all commands which are exectable
            if "list" in command.lower() and "commands" in command.lower() and "assistant" in command.lower():
                print(r"1. Open YouTube - To open YouTube using Google Chrome")
                print(r"2. Open Google - To open Google using Google Chrome")
                print(r"3. Open Chrome - To open Chrome either using Chrome.exe or using https://www.google.com")
                print(r"4. Open ChatGPT - To open ChatGPT in Chrome")
                print(r"5. Time now - To know the current Time")
                print(r"6. Date Today - To know the Date of Today")
                print(r"7. Open Wikipedia - To open Wikipedia using Chrome")
                print(r"8. Open Whatsapp - To open Web-Whatsapp")
                print(r"9. Open Telegram - To open Web-Telegram")
                print(r"10. Open {{drive-character}} Drive - To open Desire drive in your PC")
                print(r"    10.1 Make Folder - To make a Folder")
                print(r"    10.2 Make Multiple Folders - To make Multiple Folders")
                print(r"    10.3 Delete Folder - To Delete a Folder")
                print(r"    10.4 Delete Multiple Folders - To Delete Multiple a Folders")
                print(r"    10.5 Make File - To make a File")
                print(r"    10.6 Make Multiple files - To make Multiple Files")
                print(r"    10.7 Delete File - To Delete File")
                print(r"    10.8 Delete Multiple files - To Delete Multiple Files")
                print(r"    10.9 Move/Cut Folder/File - To move/cut the file/folder to another Destination in Computer")
                print(r"    10.10 Copy File - To Copy the File and Paste it into the Destination in Computer")
                print(r"    10.11 Copy Folder - To Copy the Folder and Paste it into the Destination in Computer")
                print(r"    10.12 Rename - To Rename the File/Folder")
                print(r"11. Open {{websiten-name.TLD}} website - To open Desire Website")
                print(r"12. Search {{your-search-in-YouTube}} in YouTube - To open Desire Searched page on YouTube")
                print(r"13. Tell me about {{you-query}} - To Search your Query on Google")
                print(r"14. Battery Status - To know Battery Status of your Laptop")
                print(r"15. You can also use me as a Standard Calculator by entering the problems.txt ")
                print(r"16. Search Item - To search any item in your PC or Laptop")
                print(r"17. Memory Usage - To know the Memory Usage in your Drive")
                say("Here is the list of Commands that I can Execute in this Version")

        except Exception as e:
            print("ERROR OCCURRED.")
            say("Sorry, I Can't Do This")
