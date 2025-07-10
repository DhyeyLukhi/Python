import os
import time
import keyboard

while True:
    try:
        path = input("Enter the path: ")
        if os.path.exists(path):
            items = os.listdir(path)
            for i in range(0, len(items)):
                print(f"{i}. {items[i]}")
            print("Are these items you want to rename ? ")
            print("[Y]: Yes   [N]: No    :", end="")
            confirmation = keyboard.read_event()
            if confirmation.event_type == keyboard.KEY_DOWN:
                if confirmation.name == 'y':
                    time.sleep(0.01)
                    extension = input("\nEnter the extension: ")
                    for file in range(0, len(items)):
                        print(items[file])
                        new_name = input("New Name: ")
                        old_name = path + "\\" + f"{items[file]}"
                        new_name_with_extension = path + "\\" + f"{new_name}" + f".{extension}"
                        os.rename(old_name, new_name_with_extension)

                        print("Done")

                elif confirmation.name == 'n':
                    print("Quitting the application... ")
                    quit()

        else:
            print("Path doesn't exist or other ERROR occured")

    except Exception as e:
        print(e)
