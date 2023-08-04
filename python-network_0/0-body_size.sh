#!/bin/bash
# Sends a request and displays the size of the response body
curl -sI "$1" | sed -En "s/Content-Length: (.*)/\1/p"
