# password generator
# requires least python 3.6 to use secrets

import string
from secrets import choice


def password_gen_init():
    """
    Ask user about password parameters (length and strength) and
    initializes process of generating password.

    Prints generated password.
    """
    try:
        length = int(input('\nEnter a passwords length: '))
        strength = int(input('\nEnter a passwords strength: '))
        password = generate_password(length, strength)

        if len(password) == int(length):
            print('\n-----------------------------')
            print('\nGenerated password is:\n')
            print(password.center(30))

    except ValueError:
        print('\nError. Probably wrong input.\nInputs for strength and length has to be integer type (number).')
        password_gen_init()


def generate_password(length, strength):
    """
    Generates password characters base due to chosen strength level
    than generates password with given length and strength level.

    :param length: integer >= 1
    :param strength: integer 1 - 4 inclusive
    :return: string - generated password
    """
    digit = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    symbol = string.punctuation

    if strength > 4:
        print('\nGiven password strength was too high and it was reduced to level 4.')

    if strength < 1 or length < 1:
        if strength < 1:
            print('Given strength should be 1 - 4.')
        if length < 1:
            print('Password length should be at least 1 (for level 1 strength).')
        password_gen_init()

    while True:
        if strength == 1 and length >= 1:
            pwd_base = lower
        elif strength == 2 and length >= 2:
            pwd_base = lower + upper
        elif strength == 3 and length >= 3:
            pwd_base = lower + upper + digit
        elif strength >= 4 and length >= 4:
            pwd_base = lower + upper + digit + symbol
        else:
            return print('\nSomething went wrong. Probably you gave wrong password length'
                         ' according to its strength.')

        password = ''.join(choice(pwd_base) for _ in range(length))

        if check_password(password, strength, length):
            return password


def check_password(pwd, strength, length):
    """
    Checks if generated password is correct.
    Correct password contains at least one
    character from each of characters group
    for chosen strength level.

    :param pwd: string - generated password
    :param strength: integer 1-4
    :param length: integer >= 1
    :return: bool - True if password correct, False if not.
    """
    if strength == 1 and length >= 1:
        if any(c.islower() for c in pwd):
            return pwd

    elif strength == 2 and length >= 2:
        if any(c.islower() for c in pwd) and any(c.isupper() for c in pwd):
            return pwd

    elif strength == 3 and length >= 3:
        if (any(c.islower() for c in pwd)
                and any(c.isupper() for c in pwd)
                and sum(c.isdigit() for c in pwd) >= 1):
            return pwd

    elif strength >= 4 and length >= 4:
        if (any(c.islower() for c in pwd)
                and any(c.isupper() for c in pwd)
                and sum(c.isdigit() for c in pwd) >= 1
                and any(c in string.punctuation for c in pwd)):
            return True
    return False


if __name__ == '__main__':
    print('This program will generate a random password of given length and strength.'
          '\nMinimum password length for strength in scale 1-4:\n'
          '\n1. only lowercase - 1 character'
          '\n2. lowercase and uppercase - 2 characters'
          '\n3. lowercase, uppercase and digits - 3 characters'
          '\n4. lowercase, uppercase, digits and punctuation - 4 characters'
          )

    password_gen_init()
