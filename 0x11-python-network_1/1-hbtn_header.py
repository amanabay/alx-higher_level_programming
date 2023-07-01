#!/usr/bin/python3
"""
    Module that sends a request to the URL and
    displays the value of the X-Request-Id variable
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        x_request_id = header.get('X-Request-Id')
        print(x_request_id)
