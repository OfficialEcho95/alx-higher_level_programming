
#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


def main():
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.getheader("X-Request-Id")

    print(header)


if __name__ == '__main__':
    main()
