#!/usr/bin/python3
for letter_code in range(65, 91):
    if letter_code != 69 and letter_code != 81:
        letter = chr(letter_code).lower()
        print("{}".format(letter), end="")
