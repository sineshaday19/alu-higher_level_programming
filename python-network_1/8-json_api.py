#!/usr/bin/python3
'''script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    var = sys.argv[1] if len(sys.argv) >= 2 else ""
    payload = {"q": var}
    response = requests.post(url, data=payload)
    try:
        json_data = response.json()
        if len(json_data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(
                json_data.get('id'),
                json_data.get('name')))
    except ValueError as e:
        print("Not a valid JSON")
