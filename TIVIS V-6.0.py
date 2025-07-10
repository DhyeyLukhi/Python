import os
import re
import shutil
import pyttsx3
import webbrowser
import datetime
import subprocess


def say(text):  # say: This function will speak
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return text


def explore_folders(path):
    # Iterate over all the items in the given path
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            print(item_path)  # Print the folder path

            # Recursively explore the subfolder
            explore_folders(item_path)
    return 0


def simple_folder(path):  # When you are in the diks
    try:
        name = input("Enter the name: ")
        folder_path = os.path.join(path, name)
        try:
            os.mkdir(folder_path)
            print("Fodler Created Successfuly")
            say("Folder Create, Sir")
        except Exception as e:
            if '\\' or '/' or '>' or '<' in name:
                print(r"You can't contains \,/,<,>,*,?,| in the name of the folder")
            else:
                print("ERROR to create the folder")
        return name
    except Exception as e:
        print("ERROR OCCURRED")
        say("I can't make folder there, Sir")


def multiple_folder(path):  # When you are in the diks
    try:
        number = int(input("Enter the number of folders: "))
        for i in range(0, number):
            name = input(f"Name of {i+1} Folder: ")
            folder_path = os.path.join(path, name)
            try:
                os.mkdir(folder_path)
                print("Fodler Created Successfuly")
                say("Folder Create, Sir")
            except Exception as e:
                if '\\' or '/' or '>' or '<' in name:
                    print(r"You can't contains \,/,<,>,*,?,| in the name of the folder")
                else:
                    print("ERROR to create the folder")

    except Exception as e:
        print("ERROR OCCURRED")
        say("I can't make folder there, Sir")
    return 0


def del_folder(path):  # When you are in the diks
    try:
        name = input("Enter the name: ")
        folder_path = os.path.join(path, name)
        os.rmdir(folder_path)
        print("Folder Deleted Successfuly")
        say("Folder Deleted, Sir")
    except Exception as e:
        print("ERROR FOUNDS")
        say("i can't Delete this folder, Sir")
        return


def del_multi_folder(path):  # When you are in the diks
    try:
        number = int(input("Enter the number of Fodlers: "))
        for i in range(0, number):
            name = input(f"Name of {i+1} Folder: ")
            folder_path = os.path.join(path, name)
            os.rmdir(folder_path)
            print("Folder Deleted Successfuly")
            say("Folder Deleted, Sir")

    except Exception as e:
        print("ERROR FOUNDS")
        say("I can't Delete this folder, Sir")
        return 0


def simple_file(path):  # When you are in the diks
    try:
        name = input("Name of file: ")
        exte = input("Enter the Extension: ")
        name += exte
        try:
            file_path = os.path.join(path, name)
            file = open(file_path, "w")
            file.close()
            print("File Created Successfuly")
            say("File Created, Sir")
        except Exception as e:
            if '\\' or '/' or '>' or '<' in name:
                print(r"You can't contains \,/,<,>,*,?,| in the name")
            else:
                print("ERROR to create the File")
    except Exception as e:
        print("ERROR FOUNDS")
        say("I can't Create this file, Sir")
    return 0


def multi_file(path):  # When you are in the diks
    try:
        number = int(input("Enter the number: "))
        for i in range(0, number):
            name = input(f"Name of {i+1} File: ")
            exte = input("Extension : ")
            name += exte
            try:
                file_path = os.path.join(path, name)
                file = open(file_path, "w")
                file.close()
                print("File Created Successfuly")
                say("File Created, Sir")
            except Exception as e:
                if '\\' or '/' or '>' or '<' in name:
                    print(r"You can't contains \,/,<,>,*,?,| in the name")
                else:
                    print("ERROR to create the File")
    except Exception as e:
        print("ERROR FOUNDS")
        say("I can't Create this file, Sir")
    return 0


def del_file(path):  # When you are in the diks
    try:
        name = input(f"Name of {i + 1} File: ")
        exte = input("Extension : ")
        name += exte
        file_path = os.path.join(path, name)
        os.remove(file_path)
        print("File Deleted Successfuly")
        say("File Deleted, Sir")
    except Exception as e:
        print("ERROR FOUNDS")
        say("I can't Delete this file, Sir")
    return 0


def del_multi_file(path):  # When you are in the diks
    try:
        number = int(input("Enter the Numbers: "))
        for i in range(0, number):
            name = input(f"Name of {i+1} File: ")
            exte = input(f"Extension: ")
            name += exte
            file_path = os.path.join(path, name)
            os.remove(file_path)
            print("File Deleted Successfuly")
            say("File Deleted, Sir")
    except Exception as e:
        print("ERROR FOUNDS")
        say("I can't Delete this file, Sir")
        return 0


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
    print("TIVIS formely known as Optimus")
    print("TIVIS - Your Desktop Assistant. Version 6.0")
    print("Some issues had fixed now")
    say("TIVIS is here for your Assist, Sir")


def take_command():  # This function will take command form user
    user_command = str(input("Command: "))
    return user_command


def make_folder():
    say("At which disk do you have to make a folder")
    disk = input("Enter 'c' dor C and 'e' for E disk: ")
    if 'c' in disk.lower():
        name_of_folder = input("Name of folder: ")
        try:

            folder_path = os.path.join(pathc, name_of_folder)
            try:
                os.mkdir(folder_path)
                print("Folder created successfully")
                say("Folder created, Sir")
            except Exception as e:
                if '\\' or '/' or '>' or '<' in name_of_folder:
                    print(r"You can't contains \,/,<,>,*,?,| in the name")
                else:
                    print("ERROR to create the folder")
        except Exception as e:
            tell = e
            print("Some ERROR Founds")
            say("I can't make Folder")

    if 'e' in disk.lower():
        name_of_folder = input("Entre the name of the folder: ")
        try:
            folder_path = os.path.join(pathd, name_of_folder)
            try:
                os.mkdir(folder_path)
                print("Folder created successfully")
                say("Folder created, Sir")
            except Exception as e:
                if '\\' or '/' or '>' or '<' in name_of_folder:
                    print(r"You can't contains \,/,<,>,*,?,| in the name")
                else:
                    print("ERROR to create the folder")
        except Exception as e:
            tell = e
            print("Some ERROR Founds")
            say("I can't make Folder")


def make_multiple_folder():
    say("At which disk do you have to make Folders")
    disk = input("Enter 'c' dor C and 'e' for E disk: ")
    folders = int(input("How many folders do your have to made: "))
    if 'c' in disk.lower():
        for folders in range(0, folders):
            name_of_folder = input(f"Name of {folders + 1} folder: ")
            try:
                folder_path = os.path.join(pathc, name_of_folder)
                try:
                    os.mkdir(folder_path)
                    print("Folder created successfully")
                    say("Folder created, Sir")
                except Exception as e:
                    if '\\' or '/' or '>' or '<' in name_of_folder:
                        print(r"You can't contains \,/,<,>,*,?,| in the name")
                    else:
                        print("ERROR to create the Folder")
            except Exception as e:
                tell = e
                print("Some ERROR Founds")
                say("I can't make Folder")

    if 'e' in disk.lower():
        for folders in range(0, folders):
            name_of_folder = input(f"Name of {folders + 1} folder: ")
            try:
                folder_path = os.path.join(pathd, name_of_folder)
                try:
                    os.mkdir(folder_path)
                    print("Folder created successfully")
                    say("Folder created, Sir")
                except Exception as e:
                    if '\\' or '/' or '>' or '<' in name_of_folder:
                        print(r"You can't contains \,/,<,>,*,?,| in the name")
                    else:
                        print("ERROR to create the Folder")
            except Exception as e:
                tell = e
                print("Some ERROR Founds")
                say("I can't make Folder")


def delete_folder():
    say("Which folder do you want to delete ?")
    deletefolder = input("Which folder do you want to delete: ")
    disk = input("Enter 'c' for C disk and 'e' for E disk: ")
    if 'c' in disk.lower():
        try:
            folder_path = os.path.join(pathc, deletefolder)
            os.rmdir(folder_path)
            print("Folder deleted Successfully")
            say("Folder Deleted, Sir")

        except Exception as e:
            tell = e
            print("Some ERROR Founds")
            say("I can't delete Folder")

    if 'e' in disk.lower():
        try:
            folder_path = os.path.join(pathd, deletefolder)
            os.rmdir(folder_path)
            print("Folder deleted Successfully")
            say("Folder Deleted, Sir")

        except Exception as e:
            tell = e
            print("Some ERROR Founds")
            say("I can't delete Folder")


def delete_multiple_folder():
    say("Where is the Folders ?")
    disk = input("Enter 'c' for C disk or 'e' for E disk: ")
    folders = int(input("How many Folder you have to Delete: "))
    if 'c' in disk.lower():
        for folders in range(0, folders):
            name_of_folder = input(f"Name of {folders + 1} Folder: ")
            try:
                folder_path = os.path.join(pathc, name_of_folder)
                os.rmdir(folder_path)
                print("Folder deleted Successfully")
                say("Folder Deleted, Sir")

            except Exception as e:
                tell = e
                print("Some ERROR Founds")
                say("I can't delete Folder")

    if 'e' in disk.lower():
        for folders in range(0, folders):
            name_of_folder = input(f"Name of {folders + 1} Folder: ")
            try:
                folder_path = os.path.join(pathd, name_of_folder)
                os.rmdir(folder_path)
                print("Folder deleted Successfully")
                say("Folder Deleted, Sir")

            except Exception as e:
                tell = e
                print("Some ERROR Founds")
                say("I can't delete Folder")


def make_file():
    say("At which disk do you have to make a file")
    disk = input("Enter 'c' for C disk and 'e' for E disk: ")
    if 'c' in disk.lower():
        name_of_file = input("Name of the file: ")
        filepath = os.path.join(pathc, name_of_file)
        try:
            try:
                file = open(filepath + ".txt", "w")
                file.close()
                print("File created successfully")
                say("File created, Sir")
            except Exception as e:
                if '\\' or '/' or '>' or '<' in name_of_file:
                    print(r"You can't contains \,/,<,>,*,?,| in the name")
                else:
                    print("ERROR to create the File")
        except Exception as e:
            tell = e
            print("Some ERROR Founds")
            say("I can't make the File")

    if 'e' in disk.lower():
        name_of_file = input("Name of the file: ")
        filepath = os.path.join(pathd, name_of_file)
        try:
            try:
                file = open(filepath + ".txt", "w")
                file.close()
                print("File created successfully")
                say("File created, Sir")
            except Exception as e:
                if '\\' or '/' or '>' or '<' in name_of_file:
                    print(r"You can't contains \,/,<,>,*,?,| in the name")
                else:
                    print("ERROR to create the File")
        except Exception as e:
            tell = e
            print("Some ERROR Founds")
            say("I can't make the File")


def make_multiple_file():
    say("At which disk you want to make File ?")
    disk = input("Enter 'c' for C disk or 'e' for E disk: ")
    files = int(input("How many files you want to make: "))
    if 'c' in disk.lower():
        for files in range(0, files):
            name_of_file = input(f"Name of {files + 1} File: ")
            extension = input("Enter the Extension(Example = '.txt'): ")
            name_of_file += extension
            filepath = os.path.join(pathc, name_of_file)
            try:
                try:
                    file = open(filepath + ".txt", "w")
                    file.close()
                    print("File created successfully")
                    say("File created, Sir")
                except Exception as e:
                    if '\\' or '/' or '>' or '<' in name_of_file:
                        print(r"You can't contains \,/,<,>,*,?,| in the name")
                    else:
                        print("ERROR to create the File")
            except Exception as e:
                tell = e
                print("Some ERROR Founds")
                say("I can't make the File")

    if 'e' in disk.lower():
        for files in range(0, files):
            name_of_file = input(f"Name of {files + 1} File: ")
            filepath = os.path.join(pathc, name_of_file)
            extension = input("Enter the Extension(Example = '.txt'): ")
            name_of_file += extension
            try:
                try:
                    file = open(filepath + ".txt", "w")
                    file.close()
                    print("File created successfully")
                    say("File created, Sir")
                except Exception as e:
                    if '\\' or '/' or '>' or '<' in name_of_file:
                        print(r"You can't contains \,/,<,>,*,?,| in the name")
                    else:
                        print("ERROR to create the File")
            except Exception as e:
                tell = e
                print("Some ERROR Founds")
                say("I can't make the File")


def delete_file():
    say("Which file do you want to delete ?")
    delete_file = input("Which file do you want to delete: ")
    extension = input("Enter the extension of the file(Example = '.txt'): ")
    delete_file += extension
    disk = input("Enter 'c' for C disk and 'e' for E disk: ")
    if 'c' in disk.lower():
        try:
            filepath = os.path.join(pathc, delete_file)
            os.remove(filepath)
            print("File deleted Successfully")
            say("File Deleted, Sir")
        except Exception as e:
            tell = e
            print("Some ERROR Founds")
            say("I can't Delete the File")

    if 'e' in disk.lower():
        try:
            filepath = os.path.join(pathd, delete_file)
            os.remove(filepath)
            print("File deleted Successfully")
            say("File Deleted, Sir")
        except Exception as e:
            tell = e
            print("Some ERROR Founds")
            say("I can't Delete the File")


def delete_multiple_file():
    say("Where is the Files ?")
    disk = input("Enter 'c' for C disk or 'e' for E disk: ")
    files = int(input("How many Files you have to Delete: "))
    if 'c' in disk.lower():
        for files in range(0, files):
            name_of_file = input(f"Name of {files + 1} File: ")
            extension = input("Enter the Extension(Example = '.txt'): ")
            name_of_file += extension
            try:
                filepath = os.path.join(pathc, name_of_file)
                os.remove(filepath)
                print("File deleted Successfully")
                say("File Deleted, Sir")
            except Exception as e:
                tell = e
                print("Some ERROR Founds")
                say("I can't Delete the File")

    if 'e' in disk.lower():
        for files in range(0, files):
            name_of_file = input(f"Name of {files + 1} File: ")
            extension = input("Enter the Extension(Example = '.txt'): ")
            name_of_file += extension
            try:
                filepath = os.path.join(pathc, name_of_file)
                os.remove(filepath)
                print("File deleted Successfully")
                say("File Deleted, Sir")
            except Exception as e:
                tell = e
                print("Some ERROR Founds")
                say("I can't Delete the File")


def rename(path):
    items = get_items(path)
    oldname = input("Enter existing name: ")
    oldnamepath = os.path.join(path, oldname)
    j = 0
    for item in items:
        if oldname == items[j]:
            print("Folder Founded")
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
    for item in items:
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
        elif name != items[j]:
            j += 1


def copyfile(path1):
    items = get_items(path1)
    name = input("Enter the name: ")
    j = 0
    for item in items:
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
        elif name != items[j]:
            j += 1


def copyfolder(path1):
    items = get_items(path1)
    name = input("Enter the name: ")
    j = 0
    for item in items:
        if name == items[j]:
            paths = path1 + name
            paths = os.path.join(path1, name)
            print("Folder Copied Succesfully")
            destpath = input(r"Enter the destination(e.g. C:\\User\\Yourfolder\\): ")
            try:
                shutil.copytree(paths, destpath)
                print("Folder Transfer Successful")
                break
            except Exception as e:
                print("Folder Transer Failed")
                say("Folder Transer is Failed")
                break
        elif name != items[j]:
            j += 1


pathc = "C:\\"
pathd = "D:\\"
pathf = "F:\\"

if __name__ == '__main__':  # The execution of the programme starts here
    wish()
    assist()
    print("Ready to execute your command")
    while True:
        command = take_command()
        try:
            if 'open youtube' in command.lower():  # Open youtube
                print("Executing...")
                say("Opening Youtube, Sir")
                webbrowser.open("https://www.youtube.com")

            if 'open google' in command.lower():  # Open google
                print("Executing...")
                say("Opening google, Sir")
                webbrowser.open("https://www.google.com")

            if 'open wikipedia' in command.lower():  # Open wikipedia
                print("Executing...")
                say("Opening wikipedia, Sir")
                webbrowser.open("https://www.wikipedia.com")

            if 'what is the time now' in command.lower() or 'time now' in command.lower():  # Telling the time
                print("Executing...")
                hor = int(datetime.datetime.now().strftime("%H"))
                mnt = int(datetime.datetime.now().strftime("%M"))
                if hor > 12:
                    hor = hor - 12
                    print(datetime.datetime.now().strftime(f"{hor} : {mnt} PM"))
                    say(f"The time is {hor} hours and {mnt} minutes PM")
                elif hor < 12:
                    print(datetime.datetime.now().strftime(f"{hor} : {mnt} AM"))
                    say(f"The time is {hor} hours and {mnt} minutes AM")
                elif hor == 12:
                    print(datetime.datetime.now().strftime(f"{hor} : {mnt} PM"))
                    say(f"The time is {hor} hours and {mnt} minutes PM")

            if 'what is the date' in command.lower() or 'date of today' in command.lower() or 'date today' in command.lower():
                # Date of today
                print("Executing...")
                date = datetime.date.today()
                print(date)
                say(f"Today's Date is {date}")

            if 'open chatgpt' in command.lower():  # Open chatGPT
                print("Executing...")
                say("Opening ChatGPT, Sir")
                webbrowser.open("https://chat.openai.com")

            if 'open pycharm' in command.lower() or 'open pc' in command.lower():  # Open PyCharm
                print("Executing...")
                path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.3\\bin\\pycharm64.exe"
                if os.path.exists(path):
                    say("opening PyCharm, sir")
                    subprocess.Popen(path)

            if 'open chrome' in command.lower():  # pen Chrome
                print("Executing...")
                path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                say("Opening Chrome, Sir")
                subprocess.Popen(path)

            if 'open whatsapp' in command.lower():  # Open Whatsapp
                print("Executing...")
                say("Opening Whatsapp, Sir")
                webbrowser.open("https://web.whatsapp.com/")

            if 'open telegram' in command.lower():  # Open Telegram
                print("Executing...")
                say("Opening Telegram, Sir")
                webbrowser.open("https://web.telegram.org/k/")

            if 'make folder' in command.lower() or 'make a folder' in command.lower():
                make_folder()

            if 'make multiple folder' in command.lower() or 'make multiple folders' in command.lower():
                make_multiple_folder()

            if 'delete a folder' in command.lower() or 'delete folder' in command.lower():
                delete_folder()

            if 'delete multiple folder' in command.lower() or 'delete multiple folders' in command.lower() or 'delete multi folder' in command.lower() or 'delete multi folders' in command.lower():
                delete_multiple_folder()

            if 'make file' in command.lower() or 'make a file' in command.lower():
                make_file()

            if 'make multiple file' in command.lower() or 'make multiple files' in command.lower() or 'make multi file' in command.lower() or 'make multi files' in command.lower():
                make_multiple_file()

            if 'delete a file' in command.lower() or 'delete file' in command.lower():
                delete_file()

            if 'delete multiple file' in command.lower() or 'delete multiple file' in command.lower() or 'delete multi file' in command.lower() or 'delete multi file' in command.lower():
                delete_multiple_file()

            if ('open ' in command.lower() and ' on ' in command.lower() and ' youtube' in command.lower()) or ('open ' in command.lower() and ' in ' in command.lower() and ' youtube' in command.lower()) or ('open ' in command.lower() and ' at ' in command.lower() and ' youtube' in command.lower()):
                channel = r'open (.*?) on youtube'
                match = re.search(r'open (.*?) (on|in|at) youtube', command, re.IGNORECASE)
                if match:
                    channel = match.group(1)
                    webbrowser.open(f"https://www.youtube.com/@{channel}")

            if 'tell me about' in command.lower():
                match = re.search(r'tell me about (.+)', command, re.IGNORECASE)
                if match:
                    search = match.group(1).strip()
                    search = search.replace(' ', '+')
                    webbrowser.open(f"https://www.google.com/search?q={search}")

            if 'open c drive' in command.lower():
                pathc = 'C:\\'
                items = get_items(pathc)
                print(items)
                i = 1000
                for i in range(0, i):
                    enter = str(input("Enter the Command: "))
                    try:
                        if '<exit>' in enter.lower():
                            pathc = 'C:\\'
                            break
                        elif 'make folder' in enter:
                            simple_folder(pathc)
                        elif 'make multiple folder' in enter.lower():
                            multiple_folder(pathc)
                        elif 'delete folder' in enter.lower():
                            del_folder(pathc)
                        elif 'delete multiple folder' in enter.lower():
                            del_multi_folder(pathc)
                        elif 'make file' in enter.lower():
                            simple_file(pathc)
                        elif 'make multiple file' in enter.lower():
                            multi_file(pathc)
                        elif 'delete file' in enter.lower():
                            del_file(pathc)
                        elif 'delete multiple file' in enter.lower():
                            del_multi_file(pathc)
                        elif 'rename' in enter.lower():
                            rename(pathc)
                        elif 'move the file' in enter.lower():
                            move(pathc)
                        elif 'copy the file' in enter.lower():
                            copyfile(pathc)
                        elif 'give me the list' in enter.lower():
                            items = get_items(pathc)
                            print(items)
                        else:
                            pathc = pathc + enter + '\\'
                            items = get_items(pathc)
                            print(items)
                    except Exception as e:
                        print("Something is wrong")
                        say("There is an ERROR Coming")

            if 'open d drive' in command.lower():
                pathd = 'D:\\'
                items = get_items(pathd)
                print(items)
                i = 1000
                for i in range(0, i):
                    enter = str(input("Enter the Command: "))
                    try:
                        if '<exit>' in enter:
                            pathd = 'D:\\'
                            break
                        elif 'make folder' in enter:
                            simple_folder(pathd)
                        elif 'make multiple folder' in enter.lower():
                            multiple_folder(pathd)
                        elif 'delete folder' in enter.lower():
                            del_folder(pathd)
                        elif 'delete multiple folder' in enter.lower():
                            del_multi_folder(pathd)
                        elif 'make file' in enter.lower():
                            simple_file(pathd)
                        elif 'make multiple file' in enter.lower():
                            multi_file(pathd)
                        elif 'delete file' in enter.lower():
                            del_file(pathd)
                        elif 'delete multiple file' in enter.lower():
                            del_multi_file(pathd)
                        elif 'rename' in enter.lower():
                            rename(pathd)
                        elif 'move the file' in enter.lower():
                            move(pathd)
                        elif 'copy the file' in enter.lower():
                            copyfile(pathd)
                        elif 'give me the list' in enter.lower():
                            items = get_items(pathd)
                            print(items)
                        else:
                            pathd = pathd + enter + '\\'
                            items = get_items(pathd)
                            print(items)
                    except Exception as e:
                        print("Something is wrong")
                        say("There is an ERROR Coming")

            if 'open f drive' in command.lower():
                pathf = 'F:\\'
                items = get_items(pathf)
                print(items)
                i = 1000
                for i in range(0, i):
                    enter = str(input("Enter the Command: "))
                    try:
                        if '<exit>' in enter:
                            pathf = 'F:\\'
                            break
                        elif 'make folder' in enter:
                            simple_folder(pathf)
                        elif 'make multiple folder' in enter.lower():
                            multiple_folder(pathf)
                        elif 'delete folder' in enter.lower():
                            del_folder(pathf)
                        elif 'delete multiple folder' in enter.lower():
                            del_multi_folder(pathf)
                        elif 'make file' in enter.lower():
                            simple_file(pathf)
                        elif 'make multiple file' in enter.lower():
                            multi_file(pathf)
                        elif 'delete file' in enter.lower():
                            del_file(pathf)
                        elif 'delete multiple file' in enter.lower():
                            del_multi_file(pathf)
                        elif 'rename' in enter.lower():
                            rename(pathf)
                        elif 'move the file' in enter.lower():
                            move(pathf)
                        elif 'copy the file' in enter.lower():
                            copyfile(pathf)
                        elif 'copy the folder' in enter.lower():
                            copyfolder(pathf)
                        elif 'give me the list' in enter.lower():
                            items = get_items(pathf)
                            print(items)
                        elif 'open ' in enter:
                            enter = enter.replace("open ", "")
                            pathf = pathf + f"{command}" + '\\'
                            os.startfile(pathf)
                        else:
                            pathf = pathf + enter + '\\'
                            items = get_items(pathf)
                            print(items)
                    except Exception as e:
                        print("Something is wrong")
                        say("There is an ERROR Coming")

            if 'close optimus' in command.lower() or 'turn off optimus' in command.lower() or '<exit>' in command.lower() or '<Exit>' in command.lower():
                quit()

            if 'open' in command.lower() and 'website' in command.lower():
                website = r'open (.*?) website'
                match = re.search(website, command, re.IGNORECASE)
                if match:
                    webname = match.group(1)
                    webbrowser.open(f"https://www.{webname}")

        except Exception as e:
            print("ERROR OCCURRED.")
            say("There is an ERROR coming To Execute Your Command")
