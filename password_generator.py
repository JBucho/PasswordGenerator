# password generator
# requires at least python 3.6 to use secrets

import string
from secrets import choice
from pyperclip import copy


def password_gen_init():
    """Initialize generating password process.

    Ask user about password parameters (length and strength) and
    initializes process of generating password.

    :return: string -> message containing generated password
    """
    try:
        length = int(input("\nEnter a passwords length: "))
        strength = int(input("\nEnter a passwords strength: "))

        if check_gen_conditions(length, strength):
            password = generate_password(length, strength)

            copy(password)  # Copping password to clipboard

            password_message = (
                "\n-----------------------------"
                "\nGenerated password is:\n"
                + password.center(30)
                + "\n\n*Your password has been also copied to clipboard."
            )

            return password_message

        else:
            print(
                "\nYou gave wrong parameters for password generating."
                "\nPlease, check the NOTEs and try again."
            )
            password_gen_init()

    except ValueError:
        print(
            "\nError. Wrong input.\nInputs for strength and length has to be integer type (number)."
        )
        password_gen_init()


def check_gen_conditions(length, strength):
    """ Checks if conditions for password generating are correct."""

    if strength > 4:
        strength = 4  # Reduce too high strength level to maximum level
        print(
            "\nNOTE: Given password strength was too high and it was reduced to maximum level, level 4."
        )

    if strength < 1 or length < 1:
        if strength < 1:
            print("\nNOTE: Given strength should be in range 1 - 4.")
        if length < 1:
            print(
                "\nNOTE: Password length should be at least 1 (for level 1 strength)."
            )
        return False
    elif length < strength:
        print(
            "\nNOTE: You gave wrong password length according to its strength."
            "\n\t  Length should me at least equal to strength."
        )
        return False
    else:
        return True


def generate_password(length, strength):
    """Generates password.

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

    while True:
        if strength == 1 and length >= 1:
            password_base = lower
        elif strength == 2 and length >= 2:
            password_base = lower + upper
        elif strength == 3 and length >= 3:
            password_base = lower + upper + digit
        elif strength >= 4 and length >= 4:
            password_base = lower + upper + digit + symbol
        else:
            raise ValueError(
                "Something is wrong. Please double-check your arguments for generating password. "
                "\nLength should be at least equal to strength."
            )

        password = "".join(choice(password_base) for _ in range(length))

        if check_password(password, strength, length):
            return password
        else:
            continue


def check_password(password, strength, length):
    """Checks generated password.

    Checks if generated password is correct.
    Correct password contains at least one
    character from each of characters group
    for chosen strength level.

    :param password: string -> generated password
    :param strength: integer 1-4
    :param length: integer >= 1
    :return: bool -> True if password correct, False if not.
    """
    if strength == 1 and length >= 1:
        if any(char.islower() for char in password):
            return True

    elif strength == 2 and length >= 2:
        if any(char.islower() for char in password) and any(char.isupper() for char in password):
            return True

    elif strength == 3 and length >= 3:
        if (
            any(char.islower() for char in password)
            and any(char.isupper() for char in password)
            and sum(char.isdigit() for char in password) >= 1
        ):
            return True

    elif strength >= 4 and length >= 4:
        if (
            any(char.islower() for char in password)
            and any(char.isupper() for char in password)
            and sum(char.isdigit() for char in password) >= 1
            and any(char in string.punctuation for char in password)
        ):
            return True

    return False


if __name__ == "__main__":
    print(
        "This program will generate a random password of given length and strength."
        "\nMinimum password length for strength in scale 1-4:\n"
        "\n1. only lowercase - 1 character"
        "\n2. lowercase and uppercase - 2 characters"
        "\n3. lowercase, uppercase and digits - 3 characters"
        "\n4. lowercase, uppercase, digits and punctuation - 4 characters"
    )

    outcome_message = password_gen_init()
    print(outcome_message)
