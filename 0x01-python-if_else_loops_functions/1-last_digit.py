#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = str(number)[-1]
if int(lastDigit) == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
if number > 0 and int(lastDigit) != 0:
    if int(lastDigit) < 6 :
        print(f"Last digit of {number} is {lastDigit} and less than 6 and not 0")
    elif int(lastDigit) > 5 :
        print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif number < 0 and int(lastDigit) != 0:
    print(f"Last digit of {number} is -{lastDigit} and is less than 6 and not 0")
