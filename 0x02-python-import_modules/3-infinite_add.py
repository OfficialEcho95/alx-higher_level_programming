#!/usr/bin/python3

import math

if __name__ == "__main__":
    import sys

    for i in range(len(sys.argv)-1):
        total += int(sys.argv[i+1])
        print("{}".format(total))
