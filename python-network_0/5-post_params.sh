#!/bin/bash
# takes a URL arg sends a POST request and displays the response
curl -sX POST "$1" -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD'
