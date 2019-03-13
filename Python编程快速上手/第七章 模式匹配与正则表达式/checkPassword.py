import re


def checkPassword(password):
    if len(password) >= 8:
        # 这个正则是正的枪
        passRegex = re.match(
            r'^(?=.*?\d+.*?)(?=.*?[a-z]+.*?)(?=.*?[A-Z]+.*?)(?=.*?[\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]+.*?)[\da-zA-Z\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]{8,}$',
            password)
        if passRegex != None:
            print('password is so strong')
        else:
            print('password is not secure!!')
    else:
        print('password is not secure!!')


password = input()
checkPassword(password)
