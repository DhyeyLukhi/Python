import getpass
from PyPDF2 import PdfWriter, PdfReader
import string

while True:
    try:
        writer = PdfWriter()
        file = input("Enter the path: ")
        reader = PdfReader(file)
        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])

        password = getpass.getpass("Password: ")
        writer.encrypt(password)
        with open(file, 'wb') as file:
            writer.write(file)

        print("Encrypted file")
    except Exception as e:
        print(e)

