import string
import random

letters = string.ascii_lowercase
password = ""

i = 0
while i < 12:
    password += random.choice(letters)
    i += 1
print(password)