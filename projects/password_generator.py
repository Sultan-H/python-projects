
from random import *
from string import *

def generate_strong_password(value: int, first: bool, second: bool):
    password = ""
    touse,punct = "",""
    touse += ascii_lowercase
    password += choice(touse)
    if first == True:
        touse += digits
    if second == True:
        for a in punctuation:
            if a in "!?=+-()#":
                punct += a
                touse += punct
    if first == True and value-len(password) > 0:
        password += choice(digits)
    if first == True and second == True and value-len(password) > 0 or second == True and value-len(password) > 0:
        password += choice(punct)

    if value-len(password)>0:
        for _ in range(value-len(password)):
            password += choice(touse)
    return password

numb_of_passwords = int(input("How many passwords: "))
password_length = int(input("Length of password: "))
numb_included = bool(input("True for numbers, False for not: "))
special_included = bool(input("True for special Characters, False for not: "))
if __name__ == "__main__":
    for i in range(numb_of_passwords):
        print(generate_strong_password(password_length, numb_included, special_included))