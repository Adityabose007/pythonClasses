import random

def generate_pass(length):
    LETTERS = "ADCDEFJHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*()_="

    characters = LETTERS + digits + special

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password
