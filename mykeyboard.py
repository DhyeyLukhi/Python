# import pyautogui
import time
import sys
import keyboard
import pyautogui


def nutter():
    time.sleep(2)
    for i in range(50):
        pyautogui.write("nuttertools")


def professional():
    time.sleep(2)
    for i in range(50):
        pyautogui.write("professionaltools")

def health():
    time.sleep(0.1)
    pyautogui.write("aspirine")
    pyautogui.write("preciousprotection")


def veryfast():
    time.sleep(0.3)
    pyautogui.write("getthereamazinglyfast")

def superspawn():
    time.sleep(2)
    for i in range(50):
        pyautogui.write("getthereamazinglyfast")

def thugs():
    time.sleep(2)
    for i in range(50):
        pyautogui.write("thugstools")

# ============================================================
# KEY COMBINATIONS
# ============================================================
#
# Add/remove/change combinations here.
#
# Format:
#     ("key1", "key2", "key3"): function_name
#
# The order matters of key combinations matters.


COMBINATIONS = {

    ("ctrl", "ctrl", "ctrl"): nutter,

    ("ctrl", "ctrl", "shift"): health,

    ("alt", "shift", "z"): veryfast,
    
    ("alt", "shift", "v"): superspawn,

    ("alt", "ctrl", "shift"): thugs,
        
    ("alt","alt","alt"): professional

}


# ============================================================
# SETTINGS
# ============================================================

# Maximum time allowed between two key presses.
#
# Example:
# CTRL
#   ↓ 0.5 seconds
# CTRL
#   ↓ 0.4 seconds
# CTRL
#
# = valid
#
# But if you wait longer than this, the sequence resets.

TIMEOUT = 1.5


# ============================================================
# KEY SEQUENCE MONITOR
# ============================================================

pressed_sequence = []
last_press_time = 0


def check_sequence(key):
    global pressed_sequence
    global last_press_time

    current_time = time.time()

    # --------------------------------------------------------
    # Reset if too much time passed
    # --------------------------------------------------------

    if current_time - last_press_time > TIMEOUT:
        pressed_sequence = []

    last_press_time = current_time

    # --------------------------------------------------------
    # Add the new key
    # --------------------------------------------------------

    pressed_sequence.append(key)

    # --------------------------------------------------------
    # Check whether the current sequence matches anything
    # --------------------------------------------------------

    current_sequence = tuple(pressed_sequence)

    if current_sequence in COMBINATIONS:

        # Get the function associated with this combination
        action = COMBINATIONS[current_sequence]

        # Run it
        action()

        # Clear sequence after successful match
        pressed_sequence = []

        return

    # --------------------------------------------------------
    # Check whether current sequence is still potentially valid
    #
    # Example:
    #
    # Registered:
    #     CTRL CTRL CTRL
    #
    # Current:
    #     CTRL CTRL
    #
    # We DON'T reset because another CTRL could complete it.
    # --------------------------------------------------------

    possible_match = False

    for combination in COMBINATIONS:

        if combination[:len(pressed_sequence)] == tuple(pressed_sequence):
            possible_match = True
            break

    # --------------------------------------------------------
    # If the sequence cannot possibly become a valid
    # combination, start a new sequence with this key.
    # --------------------------------------------------------

    if not possible_match:

        pressed_sequence = [key]


# ============================================================
# KEYBOARD LISTENER
# ============================================================

print("Keyboard combination monitor started.")
print("Press CTRL+C in the terminal to stop.")

keyboard.on_press(
    lambda event: check_sequence(event.name)
)

keyboard.wait()
