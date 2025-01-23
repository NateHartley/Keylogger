Simple Python Keylogger, captures keystrokes on targeted machine. <br>

> [!CAUTION]
> This is malware. Do not use without permission from machine's owner.

---

### Setup
`pip3 install keyboard`

---

### Parsing Arguments
`-h` Help option<br>
`-k` REQUIRED - Parse in a custom string used to encrypt/decrypt captured keystrokes log file<br>
`-t` REQUIRED - Parse in the number of seconds the logger will run for<br>
`-f` OPTIONAL - Each captured keystroke written on new line, if not included then will be written all on one line

#### Examples
`python3 keylogger.py -h`<br>
`python3 keylogger.py -k secret_key -t 100`<br>
`python3 keylogger.py -k secret_key -t 100 -f`

---

<br>
Exit from program to find log of captured keystrokes in .keystrokes.log
