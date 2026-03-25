import random

length = int(input("Enter password length: "))
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+?<>"

all_chars = letters + numbers + symbols
password = ""
for i in range(length):
    password += random.choice(all_chars)

print("Your password is:", password)