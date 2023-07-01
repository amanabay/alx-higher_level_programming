#!/bin/bash
# Script that sends a DELETE request to URL and displays the body of the response
curl -s "$1" -X DELETE
