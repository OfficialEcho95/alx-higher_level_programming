#!/usr/bin/pyton
def islower(c):
    for letter in range(97, 123):
        if islower(c) not in chr(letter):
            return True
        else:
            return False
