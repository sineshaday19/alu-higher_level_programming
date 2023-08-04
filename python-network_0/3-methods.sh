#!/bin/bash
# takes an argument URL and displays all allowed methods
curl -sIX OPTIONS "$1" | sed -En "s/Allow: (.*)$/\1/p"
