import random
import string


def generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    password = ''.join(random.choices(characters, k=length))
    return password


while True:
    try:
        length = int(input("Length: "))

        password = generate(length)

        print(f"Your Password is: {password}\n")
    except Exception as e:
        print(e)
