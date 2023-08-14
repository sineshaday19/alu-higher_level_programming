#!/usr/bin/python3
'''a Python script that takes in a URL, sends a
request to the URL and displays the value of the X-Request-Id variable
'''
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = response.headers._headers
        for header in headers:
            if header[0] == "X-Request-Id":
                print(header[1])
