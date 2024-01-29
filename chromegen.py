import pyautogui
import time
import random
import string
import webbrowser
import ctypes
import re

CF_TEXT = 1

kernel32 = ctypes.windll.kernel32
kernel32.GlobalLock.arg_types = [ctypes.c_void_p]
kernel32.GlobalLock.restype = ctypes.c_void_p
kernel32.GlobalUnlock.arg_types = [ctypes.c_void_p]
user32 = ctypes.windll.user32
user32.GetClipboardData.restype = ctypes.c_void_p


def get_clip6digit():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            text = ctypes.c_char_p(data)
            # data_locked = kernel32.GlobalLock(text)
            value = text.value
            return str(re.findall(r'(\d{6})', (str(value))))
    finally:
        user32.CloseClipboard()


def get_mail():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            text = ctypes.c_char_p(data)
            # data_locked = kernel32.GlobalLock(text)
            # kernel32.GlobalUnlock(data_locked)
            value = text.value
            if "@10mail.xyz" in str(value):
                match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(value))
                return str(match.group(0))
            return False
    finally:
        user32.CloseClipboard()


webbrowser.open('https://account.proton.me/signup?plan=free')
time.sleep(8)


def randomize(_option_, _length_):
    if _length_ > 0:

        # Options:6Ww$oRvfSVk95tyM  6Ww$oRvfSVk95tyM
        #       -p      for letters, numbers and symbols
        #       -s      for letters and numbers
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if _option_ == '-p':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-s':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        elif _option_ == '-l':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            string._characters_ = '1234567890'
        elif _option_ == '-m':
            string._characters_ = 'JFMASOND'

        if _option_ == '-d':
            _generated_info_ = random.randint(1, 28)
        elif _option_ == '-y':
            _generated_info_ = random.randint(1950, 2000)
        else:
            _generated_info_ = ''
            for _counter_ in range(0, _length_):
                _generated_info_ = _generated_info_ + random.choice(string._characters_)

        return _generated_info_

    else:
        return 'error'


# Username
_username_ = randomize('-s', 6) + randomize('-s', 5) + randomize('-s', 5)
pyautogui.typewrite(_username_ + '\t\t\t')
print("Username:" + _username_)

# Password

_password_ = randomize('-p', 16)
pyautogui.typewrite(_password_ + '\t' + _password_ + '\t')
print("Password:" + _password_)

pyautogui.typewrite('\n')
time.sleep(5)
pyautogui.typewrite('\t\t\t\n')

pyautogui.keyDown('ctrlleft')
pyautogui.press('t')
pyautogui.keyUp('ctrlleft')

time.sleep(4)

pyautogui.typewrite('https://dropmail.me/\n')
time.sleep(5)

newMail = True
while True:
    if not newMail:
        pyautogui.hotkey('ctrl, r')
        time.sleep(3)
    # for _ in range(34):
    #     pyautogui.typewrite('\t')
    pyautogui.typewrite('\t' * 34)
    for _ in range(16):
        pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('f5')
    time.sleep(3)

    pyautogui.typewrite('\t' * 30)
    # for _ in range(30):
    #     pyautogui.typewrite('\t')
    pyautogui.press('right')
    pyautogui.press('left')
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.press('down')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('shiftright')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyDown('ctrlleft');
    pyautogui.typewrite('c');
    pyautogui.keyUp('ctrlleft')

    newMail = get_mail()
    if newMail:
        print("10 min mail: " + newMail)
        break

pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('\t')
pyautogui.keyUp('ctrlleft')
time.sleep(1)

# .typewrite(newMail)

pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('v')
pyautogui.keyUp('ctrlleft')
pyautogui.typewrite('\n')

time.sleep(10)

pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('\t')
pyautogui.keyUp('ctrlleft')
time.sleep(15)

# pyautogui.typewrite('\t\t\t\t\t\t\t\t\t\t\t\t\t\n')

# time.sleep(5)


pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('a')
pyautogui.keyUp('ctrlleft')
pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('c')
pyautogui.keyUp('ctrlleft')

pyautogui.keyDown('ctrlleft')
pyautogui.typewrite('\t')
pyautogui.keyUp('ctrlleft')
time.sleep(5)
pyautogui.typewrite(str(get_clip6digit()) + '\n')

time.sleep(5)
pyautogui.typewrite('\n')
time.sleep(5)
pyautogui.typewrite('\t\t\t\n')
time.sleep(1)
pyautogui.typewrite('\t\n')

print(_username_ + "@proton.me" + '\n' + _password_)

logfile = open("accLog.txt", "a")
logfile.write('new mail - ' + _username_ + "@proton.me" + '\n' + 'new pass - ' + _password_ + "\n")
logfile.close()
