#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


def main():
    result = requests.get(sys.argv[1])
    header = result.headers.get("X-Request-Id")

    print(header)


if __name__ == '__main__':
    main()
