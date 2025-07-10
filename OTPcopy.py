import pyperclip
import re
from pynput import keyboard
import time


def on_activate():
    try:
        time.sleep(0.2)  # Introducing a small delay before reading the clipboard
        user_input = pyperclip.paste()

        patterns = [
            r'Dear Customer, (\d+)',
            r'Dear Customer,(\d+)',
            r'OTP: (\d+)',
            r'OTP is (\d+)',
            r'PIN: (\d+)',
            r'PIN is (\d+)',
            r'OTP:(\d+)',
            r'PIN:(\d+)',
            r'Password is (\d+)',
            r'Password is(\d+)'
            # Add more patterns here if needed
        ]

        found_numbers = []
        for pattern in patterns:
            numbers = re.findall(pattern, user_input)
            found_numbers.extend(numbers)

        found_numbers = [int(num) for num in found_numbers]

        if found_numbers:
            numbers_str = ' '.join(str(num) for num in found_numbers)
            pyperclip.copy(numbers_str)

    except Exception as e:
        pass


def for_canonical(f):
    return lambda k: f(l.canonical(k))


hotkey = '<ctrl>+c'


with keyboard.GlobalHotKeys({
        hotkey: on_activate
}) as l:
    l.join()

