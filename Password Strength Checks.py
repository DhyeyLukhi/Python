import string
import keyboard
import time


# This function check the password's strength
def check_password_strength(password):
    lower_alpha_count = upper_alpha_count = number_count = special_char_count = 0
    for char in list(password):  # Couting the lower, upper, numeric and speical characters
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        else:
            special_char_count += 1
    strength = 0
    remarks = ''

    # Checking the strength of password
    if lower_alpha_count >= 1:
        strength += 1
    if upper_alpha_count >= 1:
        strength += 1
    if number_count >= 1:
        strength += 1
    if special_char_count >= 1:
        strength += 1
    if len(password) >= 10:
        strength += 1

    # Adding remarks
    if strength == 1:
        remarks = "That's not a good password. You should consider making a tougher password."
    elif strength == 2:
        remarks = "Your password is okay, but it can be improved a lot"
    elif strength == 3:
        remarks = "Your password is hard to guess. But you can make it even more secure"
    elif strength == 4:
        remarks = "What a Password man, "
    elif strength == 5:
        remarks = "Now that's one hell of a strong password !!! Hackers don't have a chance guessing that password."

    print("Your password has:-")
    print(f"{lower_alpha_count} lowercase letters")
    print(f"{upper_alpha_count} uppercase letters")
    print(f"{number_count} digits")
    print(f"{special_char_count} special characters")
    print(f"Password score: {strength}/5")
    print(f"Remarks: {remarks}")

    return True


# Only this allowed_keys will be allowed in the password, other types of key press will be removed
allowed_keys = (
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '0123456789'
    r'!@#$%^&*()_+-=[]{}|;:\'",.<>?/'
)
password = []


print("===== Welcome to Password Strength Checker =====")
print("Do you want to continue ?")
print("[Y]: Yes      [N]: No           Answer: ", end="")

while True:
    key = keyboard.read_event()  # Read the key pressed by the user
    time.sleep(0.1)
    if key.event_type == keyboard.KEY_DOWN:  # If user press any key
        if key.name == 'y' or key.name == 'Y':  # And key is 'Y'
            print("\nEnter your Password: ", end="")
            while True:
                key = keyboard.read_event(suppress=True)  # This will ask user for the password, but it won't show the password and key pressed by the user on the prompt
                if key.event_type == keyboard.KEY_DOWN:
                    # If key pressed by the user is not 'eneter', 'backspace' and key is in allowed_keys
                    if key.name != 'enter' and key.name != 'backspace' and key.name in allowed_keys:  #
                        password.append(key.name)
                    elif key.name == 'backspace':
                        password.pop()
                    elif key.name == 'enter':
                        if not password:  # If user don't enter anything in password
                            print("Please enter the Password")
                        elif password:
                            check_password_strength(password=password)

        elif key.name == 'n' or key.name == 'N':  # And key is 'N'
            print("\nExiting from the Code....")
            break

        else:
            print("\nPlease try again !!!")
