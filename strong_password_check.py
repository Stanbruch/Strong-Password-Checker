import re

#strong password

passStrong = False
def passwordStrength():
    #Enter password
    passwordText = input('Enter password: ')

    #Strength check
    charRegex = re.compile(r'(\w{8,})')
    lowerRegex = re.compile(r'[a-z]+')
    upperRegex = re.compile(r'[A-Z]+')
    digitRegex = re.compile(r'[0-9]+')

    if charRegex.findall(passwordText) == []:
        print('Password must contain at least 8 characters, 1 lowercase, 1 uppercase and 1 number. Try again.')
    elif lowerRegex.findall(passwordText) == []:
        print('Password must contain at least 1 lowercase character, 1 uppercase and 1 number. Try again')
    elif upperRegex.findall(passwordText) == []:
        print('Password must contain at least 1 uppercase character and 1 number. Try again.')
    elif digitRegex.findall(passwordText) == []:
        print('Password must contain at least 1 number. Try again.')
    else:
        print('Your password is strong.')
        global passStrong #Set passStrong True, succes input.
        passStrong = True
        return
while not passStrong: #Again until password is strong enough.
    passwordStrength()
