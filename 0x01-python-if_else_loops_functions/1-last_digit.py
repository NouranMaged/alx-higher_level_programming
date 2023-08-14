#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = str(number)[-1]
if int(l) == 0:
    print(f"Last digit of {number} is {l} and is 0")
if number > 0 and int(l) != 0:
    if int(l) < 6:
        print(f"Last digit of {number} is {l} and less than 6 and not 0")
    elif int(l) > 5:
        print(f"Last digit of {number} is {l} and is greater than 5")
elif number < 0 and int(l) != 0:
    print(f"Last digit of {number} is -{l} and is less than 6 and not 0")
