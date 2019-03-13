# pw.py an insecure password locker program
import pyperclip as pyperclip

passWord = {
    'email': 'cwqdwqd',
    'qq': '222345',
    'wx': '23456sdasdsasa'
}

import sys

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in passWord:
    pyperclip.copy(passWord[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('none')

# 挺有用的
