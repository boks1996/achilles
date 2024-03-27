#!/usr/bin/env python3

import argparse
import requests
import validators
parser = argparse.ArgumentParser(description = "The Achilles HTML Vulnerability Analyzer Version 1.0")
parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
parser.add_argument("url", type = str, help="The URL of the HTML to analyze.")
args = parser.parse_args()
print(args.url)

url = args.url
if validators.url(url):
  result_HTML = requests.get(url).text
  print(results_HTML)
else:
  print("Invalid URL. Please include full URL with the scheme.")
