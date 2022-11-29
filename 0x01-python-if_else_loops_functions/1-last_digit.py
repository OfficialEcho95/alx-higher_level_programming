#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
#print("last digit of {} is {}".format(number, last))
if last > 5:
    print("last digit of {} is {} ".format(number, last) + "and is greater than 5")
elif last == 0:
    print("last digit of {} is {} ".format(number, last) + "and is 0")
else:
    print("last digit of {} is {} ".format(number, last) + "and is less than 6 and not 0")
