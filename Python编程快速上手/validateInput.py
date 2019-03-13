while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print('please enter a number for your age.')

while True:
    print("Select a new passwd (letters and numbers only):")
    password = input()
    if password.isalnum():
        break
    print('please enter number or letters for your passwd.')
