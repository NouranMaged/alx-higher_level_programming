#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)[-1]
if int(last) == 0:
    print(f"Last digit of {number} is {last} and is 0")
if number > 0 and int(last) != 0:
    if int(last) < 6:
        print(f"Last digit of {number} is {last} and less than 6 and not 0")
    elif int(last) > 5:
        print(f"Last digit of {number} is {last} and is greater than 5")
elif number < 0 and int(last) != 0:
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
