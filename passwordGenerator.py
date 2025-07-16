import random



def generate_pass(len):
    LETTERS = "ADCDEFJHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*()_="

    characters = LETTERS + digits + special

    password = ""

    for _ in range(len):
        pasword += random.choice(characters)

    return password


# task1 : - 