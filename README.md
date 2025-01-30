Keylogger - captures user's keystrokes on a targeted machine. <br>

> [!CAUTION]
> This is malware. Do not use without permission from machine's owner.

---

### Setup and basic run
```
pip3 install keyboard
pip3 install cryptography

python3 keylogger.py
```

---

### Parsing arguments
`-h`       Help option<br>
`-f`       Optional - Writes each captured keystroke on new line, else all is written on one line<br>
`-t`       Optional - Number of seconds the keylogger will run for<br>
`-e [key]` Optional - Key used to encrypt log file contents<br>
`-d [key]` Optional - Key used to decrypt log file contents<br>

#### Examples
```
python3 keylogger.py -h

python3 keylogger.py -e secret_key -t 100 -f

python3 keylogger.py -d secret_key
```
*Please note when decrypting, only the `-d` flag should be parsed.*

---

<br>
Program can be exited by pressing the `#` key, or by waiting for the inputted timer to run out.<br>
Captured keystrokes can be found in .process.log
