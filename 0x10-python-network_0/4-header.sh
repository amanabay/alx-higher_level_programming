#!/bin/bash
# Script that takes in a URL as an argument, sends a GET request, displays the body of the response(Using header variable)
curl -s -H "X-School-User-Id: 98" "$1"
