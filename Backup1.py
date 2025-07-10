import os
import re
import shutil
import keyboard
import pyttsx3
import webbrowser as web
import datetime
import subprocess
import psutil
import requests
import wikipedia as wiki


def search(path, item):
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


def make_folder(path_create_folder):  # When you are in the diks
    name_create_folder = input("Enter the name: ")
    try:
        if "\\" in name_create_folder.lower() or "/" in name_create_folder.lower() or "<" in name_create_folder.lower() or ">" in name_create_folder.lower() or ":" in name_create_folder.lower() or "*" in name_create_folder.lower() or "?" in name_create_folder.lower() or "|" in name_create_folder.lower() or "'" in name_create_folder.lower():
            print(r"Name cannot contain '\', '/', '<', '>', ':', '*', '|', '?', '' ")
            say("That's not possible")
            print(r"Name cannot contain \\, /, <, >, :, *, ?, |, ''")
            say("That's not possible")

        else:
            folder_path = os.path.join(path_create_folder, name_create_folder)
            os.mkdir(folder_path)
            print("Fodler Created Successfuly")
            say("Folder Create, Sir")
            return 0

    except Exception as e:
        print("There is an ERROR coming to create a folder")
        say("There is an ERROR for Folder")
        return 1


def multiple_folder(path_create_folders):  # When
    # you are in the diks
    number_create_folders = int(input("Enter the number of folders: "))
    for i in range(0, number_create_folders):
        name_create_folders = input(f"Name of {i + 1} Folder: ")

        if "\\" in name_create_folders.lower() or "/" in name_create_folders.lower() or "<" in name_create_folders.lower() or ">" in name_create_folders.lower() or ":" in name_create_folders.lower() or "*" in name_create_folders.lower() or "?" in name_create_folders.lower() or "|" in name_create_folders.lower() or "'" in name_create_folders.lower():
            print(r"Name cannot contain '\', '/', '<', '>', ':', '*', '|', '?', '' ")
            say("That's not possible")
            print(r"Name cannot contain \\, /, <, >, :, *, ?, |, ''")
            say("That's not possible")

        else:
            try:
                folder_path = os.path.join(path_create_folders, name_create_folders)
                os.mkdir(folder_path)
                print("Fodler Created Successfuly")

            except Exception as e:
                print("There is an ERROR coming to create a folder")
                say("There is an ERROR for Folder")

        if i == number_create_folders - 1:
            say("Folders are Created Successfully, sir")


def delete_folder(path_delete_folder):  # When you are in the diks
    try:
        name_delete_folder = input("Enter the name: ")
        folder_path = os.path.join(path_delete_folder, name_delete_folder)
        if os.path.exists(folder_path):
            items_in_folder = os.listdir(folder_path)
            if not items_in_folder:
                shutil.rmtree(folder_path)
                print("Folder Deleted Successfuly")
            elif items_in_folder:
                print("There are some items founded inside the folder")
                print("Are you sure Do you want to Delete the folder?")
                print("[Y]- Yes  [N]- No: ", end='')
                key = keyboard.read_event()
                if key.event_type == keyboard.KEY_DOWN:
                    if key.name == 'Y' or key.name == 'y':
                        shutil.rmtree(folder_path)
                        print("\nFolder Deleted Successfuly")
                        say("Folder Deleted, Sir")

                    elif key.name == 'N' or key.name == 'n':
                        print("\nFolder is not deleted")
                        say("Your Folder is not Deleted, Sir")

        return 0

    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR for this")
        return 1


def delete_multiple_folders(path_delete_folders):  # When you are in the disk
    try:
        number_delete_folders = int(input("Enter the number of Fodlers: "))
        for i in range(0, number_delete_folders):
            name = input(f"Name of {i + 1} Folder: ")
            folder_path = os.path.join(path_delete_folders, name)
            if os.path.exists(folder_path):
                items_in_folder = os.listdir(folder_path)
                if not items_in_folder:
                    shutil.rmtree(folder_path)
                    print("Folder Deleted Successfuly")
                    say("Folder Deleted Successfuly")

                elif items_in_folder:
                    print("There are some items founded inside the folder")
                    print("Are you sure you want to delete the folder?")
                    print("[Y]- Yes  [N]- No: ", end='')
                    key = keyboard.read_event()
                    if key.event_type == keyboard.KEY_DOWN:
                        if key.name == 'Y' or key.name == 'y':
                            shutil.rmtree(folder_path)
                            print("\nFolder Deleted Successfuly")
                            say("Folder Deleted Successfuly")
                        elif key.name == 'N' or key.name == 'n':
                            print("\nFolder is not Deleted")
                            say("Your Folder is not Deleted, Sir")

            if i == number_delete_folders - 1:
                say("Folders are Deleted Successfuly, sir")

    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR for this")


def make_file(path_create_file):  # When you are in the diks
    try:
        name_create_file = input("Name of file(without extension): ")
        if "\\" in name_create_file.lower() or "/" in name_create_file.lower() or "<" in name_create_file.lower() or ">" in name_create_file.lower() or ":" in name_create_file.lower() or "*" in name_create_file.lower() or "?" in name_create_file.lower() or "|" in name_create_file.lower() or "'" in name_create_file.lower():
            print(r"Name cannot contain '\', '/', '<', '>', ':', '*', '|', '?', '' ")
            say("That's not possible")

        else:
            extension = input("Extension: ")
            name_create_file += extension
            file_path = os.path.join(path_create_file, name_create_file)
            with open(file_path, "w") as file:
                pass
            print("File Created Successfuly")
            say("File Created, Sir")
            return 0

    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR for this")
    return 1


def multi_file(path_create_files):  # When you are in the diks
    try:
        number_create_files = int(input("Enter the number: "))
        for i in range(0, number_create_files):
            name_create_files = input(f"Name of {i + 1} File(without extension): ")
            if "\\" in name_create_files.lower() or "/" in name_create_files.lower() or "<" in name_create_files.lower() or ">" in name_create_files.lower() or ":" in name_create_files.lower() or "*" in name_create_files.lower() or "?" in name_create_files.lower() or "|" in name_create_files.lower() or "'" in name_create_files.lower():
                print(r"Name cannot contain '\', '/', '<', '>', ':', '*', '|', '?', '' ")
                say("That's not possible")

            else:
                extension = input("Extension : ")
                name_create_files += extension
                file_path = os.path.join(path_create_files, name_create_files)
                with open(file_path, "w") as file:
                    pass
                print("File Created Successfuly")

            if i == number_create_files - 1:
                say("Files are Created Successfully, sir")

    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR for this")


def delete_file(path_delete_file):  # When you are in the diks
    try:
        name_delete_file = input(f"Name of File(without extension): ")
        extension = input("Extension : ")
        name_delete_file += extension
        file_path = os.path.join(path_delete_file, name_delete_file)
        os.remove(file_path)
        print("File Deleted Successfuly")
        say("File Deleted, Sir")
    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR to do this")
    return 1


def delete_multiple_files(path_delete_files):  # When you are in the diks
    try:
        number_delete_files = int(input("Enter the Numbers: "))
        for i in range(0, number_delete_files):

            name_delete_files = input(f"Name of {i + 1} File(without extension): ")
            extension = input("Extension: ")
            name_delete_files += extension
            file_path = os.path.join(path_delete_files, name_delete_files)
            os.remove(file_path)
            print("File Deleted Successfuly")

            if i == number_delete_files - 1:
                say("Files are Deleted Successfully, sir")

    except Exception as e:
        print("ERROR FOUNDS")
        say("There is an ERROR to do this")


def get_items(directory):  # Get the list of all The items available in the directory
    items_of_folder = []
    for item_in_folder in os.listdir(directory):
        item_path = os.path.join(directory, item_in_folder)
        items_of_folder.append(item_in_folder)
    return items_of_folder


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
    old_name = input("Enter existing name: ")
    old_name_path = os.path.join(path, old_name)
    # j = 0
    if old_name in items:
        print("Item Founded")
        new_name = input("Enter new name: ")
        new_name_path = os.path.join(path, new_name)
        try:
            os.rename(old_name_path, new_name_path)
            print("Rename Successfull")
        except Exception as e:
            print("RENAME Unsuccessful")


def move(path):
    items_of_folder = get_items(path)
    name_move_item = input("Enter the name: ")
    if name_move_item in items_of_folder:
        print("File Founded")
        old_path = os.path.join(path, name_move_item)
        new_path = input(r"Enter the Destination(e.g. C:\\User\\yourfolder\\): ")
        new_path = os.path.join(path, new_path)

        try:
            shutil.move(old_path, new_path)
            print("File Moved Successfull")

        except Exception as e:
            print("File Moving Unsuccessful")


def copy_file(path1):
    items_of_folder = get_items(path1)
    name_copy_file = input("Enter the name: ")
    if name_copy_file in items_of_folder:
        path2 = os.path.join(path1, name_copy_file)
        print("File Founded")
        destination_path = input(r"Enter the destination(e.g. C:\\User\\Yourfolder\\): ")
        try:
            shutil.copy(path2, destination_path)
            print("File Transfer Successful")
        except Exception as e:
            print("File Transer Failed")
            say("File Transer is Failed")


def copy_folder(path):
    items_of_folders = os.listdir(path)
    name_copy_folder = input("Enter the name of the folder: ")
    if name_copy_folder in items_of_folders:
        path1 = os.path.join(path, name_copy_folder)
        print("Folder Founded")
        destination_path = input(r"Enter the Destinantion(e.g. C:\\User\\Your Folder\\): ")
        try:
            shutil.copytree(path1, os.path.join(destination_path, name_copy_folder))
            print("Folder Transferd to Destination")
        except Exception as e:
            print("Copy or Transfer of the folder is Failed")
            say("There is an Error for this")


def website(number):
    websites = ["https://www.youtube.com", "https://www.google.com", "https://www.wikipedia.org",
                "https://chat.openai.com", "https://web.whatsapp.com/", "https://web.telegram.org/k/"]
    sitename = ["YouTube", "Google", "Wikipedia", "ChatGPT", "Whatsapp", "Telegram"]
    web.open_new_tab(websites[number])
    print("Executing...")
    say(f"Opening {sitename[number]}, sir")

    return 0


def notepad():
    values = []
    i = 0
    while True:
        temp = input("--> ")
        values.append(temp)
        i += 1
        if '<>/ save the file /<>' in temp.lower():

            file_name = input("Enter the file name: ")
            with open(file_name, "w") as file:
                for _ in range(0, i - 1):
                    file.write(values[_])
                    file.write('\n')
            print("File will be available when you close the assistant")
            break

        if '<>/ Deactivate temp Notepad /<>' in temp.lower():
            break


def youtube_search(youtube_query):
    try:
        start = "search"
        end = "in youtube"
        pattern = re.compile(f"{re.escape(start)}(.*?){re.escape(end)}")
        match = pattern.search(youtube_query)
        if match:
            youtube_search = match.group(1).strip()
            youtube_search = youtube_search.replace(" ", "+")
            web.open(f"https://www.youtube.com/results?search_query={youtube_search}")
    except Exception as e:
        print("I can't Search this")
        say("I can't Search this query")


def website_open(website):
    match = re.search(f"open (.*?) website", website, re.IGNORECASE)
    if match:
        webname = match.group(1)
        try:
            response = requests.get(f"https://www.{webname}")

            if 200 <= response.status_code <= 299:
                print(f"Opening {webname} website")
                web.open(f"https://www.{webname}")

        except Exception as e:
            print("It is an ERROR, Check the URL")
            say("Please check the URL again")


def battery_checker():
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


def memory_checker():
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


def time():
    try:
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
    except Exception as e:
        print("I can't get the time, Sorry")
        say("I can't get the time at this moment")


def date():
    try:
        date = datetime.date.today()
        print(f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')}/{datetime.datetime.now().strftime('%G')}")
        print(f"Day : {datetime.datetime.now().strftime('%A')}")
        print(f"Month : {datetime.datetime.now().strftime('%B')}")
        say(f"Today's Date is {date}")
        say(f"Day is {datetime.datetime.now().strftime('%A')}")

    except Exception as e:
        print("I can't get the date, Sorry")
        say("I can't get the date at this moment")


def google_search(google_query):
    try:
        match1 = re.search(r"search (.+) on google", google_query, re.IGNORECASE)

        if match1:
            search = match1.group(1).strip()
            search = search.replace(" ", "+")
            web.open(f"https://www.google.com/search?q={search}")

        elif not match1:
            try:
                match2 = re.search(r'tell me about (.+)', google_query, re.IGNORECASE)

                if match2:
                    search = match2.group(1).strip()
                    search = search.replace(" ", "+")
                    web.open(f"https://www.google.com/search?q={search}")

            except Exception as e:
                print("I can't search this")
                say("I can't search you query")

    except Exception as e:
        try:
            match3 = re.search(r'tell me about (.+)', google_query, re.IGNORECASE)

            if match3:
                search = match3.group(1).strip()
                search = search.replace(" ", "+")
                web.open(f"https://www.google.com/search?q={search}")

        except Exception as e:
            print("I can't search this")
            say("I can't search you query")


def wikipedia_search(wikipedia_query):
    wikitemp = wikipedia_query
    content = re.search(r'tell me about (.+)', wikipedia_query, re.IGNORECASE)
    if content:
        page = content.group(1)
        try:
            article = wiki.summary(page, auto_suggest=False)
            article = article.replace('. ', '.\n')
            print(f"\n\n{article} \n\n")
            url = wiki.page(page, auto_suggest=False).url
            print(f"More Information: {url}")
            print(f"More Information: https://www.google.com/search?q={page.replace(' ', '+')}")

        except Exception as e:
            google_search(wikitemp)


def command_list():
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
    print(r"    10.13 <exit> - To Exit from the Drive")
    print(r"11. Open {{websiten-name.TLD}} website - To open Desire Website")
    print(r"12. Search {{your-search-in-YouTube}} in YouTube - To open Desire Searched page on YouTube")
    print(r"13. Tell me about {{you-query}} - To Search your Query on Google")
    print(r"14. Battery Status - To know Battery Status of your Laptop")
    print(r"15. You can also use me as a Standard Calculator by entering the problems.txt ")
    print(r"16. Search Item - To search any item in your PC or Laptop")
    print(r"17. Memory Usage - To know the Memory Usage in your Drive")
    print(r"18. Activate Temporary Notepad - To Activate a Temporary Notaped")
    print(r"    18.1 <>/ Save the File /<> - To save the file")
    print(r"    18.2 <>/ Deactivate Temp Notepad /<> - To Deactivate Temporary Notepad without saving the file")
    say("Here is the list of Commands that I can Execute in this Version")


if __name__ == "__main__":
    # wish()
    # assist()
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
                time()

            # Date Getting Function    # Date of today and now Day of week
            if ("date" in command.lower() and "today" in command.lower()) or ("day" in command.lower() and "today" in command.lower()) or ("day" in command.lower() and "week" in command.lower()):
                date()

            # Open ChatGPT in chrome
            if "open chatgpt" in command.lower():  # Open chatGPT
                website(3)

            # This is not for everyone
            if "open pycharm" in command.lower() or "open pc" in command.lower():  # Open PyCharm
                path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.3\\bin\\pycharm64.exe"
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
                youtube_search(command)

            # Do you want to search on Google? Don't worry this will do
            if "search" in command.lower() and "on google" in command.lower():
                google_search(command)

            # Search your query in Wikipedia
            if "tell me about" in command.lower():
                wikipedia_search(command)

            # This can open any Drive you want inyour PC
            if "open" in command.lower() and "drive" in command.lower():
                drive = re.search(f"open (.+) drive", command.lower(), re.IGNORECASE)
                if drive:
                    path = drive.group(1).strip()
                    path = path.upper()
                    path = path + ":" + "\\"
                    items = get_items(path)
                    for i in range(0, len(items)):
                        print(f"{i + 1}. {items[i]}")
                    while True:

                        enter = str(input(f"{path}> "))
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
                                delete_multiple_folders(path)

                            elif "make" in enter.lower() and "file" in enter.lower() and "multiple" not in enter.lower():
                                make_file(path)

                            elif "make" in enter.lower() and "multiple" in enter.lower() and "file" in enter.lower():
                                multi_file(path)

                            elif "delete" in enter.lower() and "file" in enter.lower() and "multiple" not in enter.lower():
                                delete_file(path)

                            elif "delete" in enter.lower() and "multiple" in enter.lower() and "file" in enter.lower():
                                delete_multiple_files(path)

                            elif "rename" in enter.lower():
                                rename(path)

                            elif ("move" in enter.lower() and " file" in enter.lower()) or ("cut" in enter.lower() and " file" in enter.lower()) or ("move" in enter.lower() and " folder" in enter.lower()) or ("cut" in enter.lower() and " folder" in enter.lower()):
                                move(path)

                            elif "copy" in enter.lower() and "file" in enter.lower():
                                copy_file(path)

                            elif "copy" in enter.lower() and "folder" in enter.lower():
                                copy_folder(path)

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
                                time()

                            elif ("date" in enter.lower() and "today" in enter.lower()) or ("day" in enter.lower() and "today" in enter.lower()) or ("day" in enter.lower() and "week" in enter.lower()):
                                date()

                            elif "give" in enter.lower() and "list" in enter.lower():
                                items = get_items(path)
                                for i in range(0, len(items)):
                                    print(f"{i + 1}. {items[i]}")

                            elif "open" in enter.lower() and "website" in enter.lower():
                                website_open(enter)

                            # It is able to check the battery status
                            elif "battery" in enter.lower() and "status" in enter.lower():
                                battery_checker()

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
                                memory_checker()

                            # Here us the list of all commands which are exectable
                            elif "list" in enter.lower() and "commands" in enter.lower() and "assistant" in enter.lower():
                                command_list()

                            elif "search" in enter.lower() and "in youtube" in enter.lower():
                                youtube_search(enter)

                            # Do you want to search on Google? Don't worry this will do
                            elif "search" in enter.lower() and "on google" in enter.lower():
                                google_search(enter)

                            else:
                                name = re.search(r"open (.+)", enter, re.IGNORECASE)
                                name = name.group(1).strip()

                                for folders in items:
                                    if folders.lower() == name.lower():

                                        if os.path.isdir(os.path.join(path, folders)):
                                            try:
                                                path = os.path.join(path, folders)
                                                items = get_items(path)
                                                for i in range(0, len(items)):
                                                    print(f"{i + 1} {items[i]}")
                                                print(f"Path = {path}")
                                            except Exception as e:
                                                pass

                                        if os.path.isfile(os.path.join(path, folders)):
                                            try:
                                                os.startfile(os.path.join(path, folders))

                                            except Exception as e:
                                                print(e)

                        except Exception as e:
                            pass

            # This can open any website
            if "open" in command.lower() and "website" in command.lower():
                website_open(command)

            # It is able to check the battery status
            if "battery" in command.lower() and "status" in command.lower():
                battery_checker()

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
                memory_checker()

            # Temporary Notepad is here
            if ('activate' in command.lower() and 'temporary' in command.lower() and 'notepad' in command.lower()) or ('activate' in command.lower() and 'temp' in command.lower() and 'notepad' in command.lower()):
                notepad()

            # Here us the list of all commands which are exectable
            if "list" in command.lower() and "commands" in command.lower() and "assistant" in command.lower():
                command_list()

        except Exception as e:
            print("ERROR OCCURRED.")
            say("Sorry, I Can't Do This")
