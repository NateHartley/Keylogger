Keylogger - captures user's keystrokes on a targeted machine. <br>

> [!CAUTION]
> This is malware. Do not use without permission from machine's owner.

---

### Setup and run
`pip3 install keyboard`<br>
`python3 keylogger.py`

---

### Parsing arguments
`-h` Help option<br>
`-k` Optional - Key used to encrypt/decrypt captured keystrokes log file<br>
`-t` Optional - Number of seconds the keylogger will run for<br>
`-f` Optional - Writes each captured keystroke on new line, else it is all written all on one line

#### Examples
`python3 keylogger.py -h`<br>
`python3 keylogger.py -k secret_key -t 100`<br>
`python3 keylogger.py -k secret_key -t 100 -f`

---

<br>
Exit program to find captured keystrokes in .keystrokes.log
