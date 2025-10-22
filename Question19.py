import re

p = input("Enter password: ")

pat = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$'

if re.match(pat, p):
    print("Valid password")
else:
    print("Invalid password")
