import re

def phoneNumberValidator(number):
    pattern='^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$'
    if re.match(pattern,number):
        print("Valid number")
    else:
        print("Invalid Number")
    return

def emailValidator(email):
    pattern="^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z]{3,18}[.][a-z]{2,3}$"
    if re.match(pattern,email):
        return True
    return False