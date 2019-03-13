# phoneAndEmail - Find phone number and email addresses on the clipboard

import pyperclip
import re

phoneRegex = re.compile(r"(" "\n"
                        r"(\d{3}|\(\d{3}\))?        # area code" "\n"
                        r"(\s|-|\.)?" "\n"
                        r"(\d{3})" "\n"
                        r"(\s|-|\.)?" "\n"
                        r"(\d{4})" "\n"
                        r"(\s*(ext|x|ext\.)\s*(\d{2,5}))?" "\n"
                        r")", re.VERBOSE)

# TODO: create email regex.

emailRegex = re.compile(r'' '\n'
                        r'[a-zA-Z0-9._%+-]+' '\n'
                        r'@' '\n'
                        r'[a-zA-Z0-9.-]+' '\n'
                        r'(\.[a-zA-Z]{2,4})' '\n', re.VERBOSE)
# TODO: Find  matches in clipboard text.

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNum = ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# TODO: Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No number or email found.')
