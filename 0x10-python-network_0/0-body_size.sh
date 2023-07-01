#!/usr/bin/bash
# Script that takes in URL, sends request and displays size of body of response
curl -s "$1" | wc -c
