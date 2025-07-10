import os.path
from PIL import Image
from rembg import remove

i = 1
while True:
    inputimage = input("Enter the Path of Image: ")

    if os.path.exists(inputimage):
        i += 1
        outputimage = inputimage + ".png"  # Change the output image file path here
        imp = Image.open(inputimage)
        output = remove(imp)
        output.save(outputimage)
    else:
        print(f"{inputimage} Doesn't exist")
