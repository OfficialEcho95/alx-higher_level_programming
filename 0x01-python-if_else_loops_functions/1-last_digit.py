#!/usr/bin/python3
'''The last digit'''

import random
number = random.randint(-10000, 10000)
last = abs(number) % 10

if number < 0:
    last = -last
if last > 5:
    print("Last digit of {} is {}".format(number, last)
          + " and is greater than 5")
elif last == 0:
    print("Last digit of {} is {}".format(number, last) + " and is 0")
else:
    print("Last digit of {} is {}".format(number, last)
          + " and is less than 6 and not 0")
