import shutil
import time
import os
from stegano import lsb

while True:
    print("[1]: Secret message  [2]: Message reveal:  ")
    choice = input("Enter the choice: ")
    try:
        if choice == "1":
            time.sleep(1)
            image = input("Enter the path of image: ")
            message = input("Enter the message: ")
            name_of_file = input("Enter the name of the image: ")
            path_image = input("Enter the path of Secret image:")
            secret = lsb.hide(image=image, message=message)
            secret.save(name_of_file+".png")
            image_path = os.getcwd()+f"\\{name_of_file}"+".png"
            shutil.move(image_path, path_image)

        elif choice == "2":
            time.sleep(1)
            reveal = input("Enter the message path: ")
            print(f"Your Message: \n{lsb.reveal(reveal)}")
        else:
            print("Wrong input, try agian")

    except Exception as e:
        print(e)
