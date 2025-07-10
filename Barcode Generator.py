import barcode
from barcode.writer import ImageWriter

number = input("CODE: ")
formate = barcode.get_barcode_class('upc')
my_barcode = formate(number, writer=ImageWriter())
my_barcode.save("Barcode")

from PIL import Image
Image.open("Barcode.png")