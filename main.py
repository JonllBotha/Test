#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    url = 'https://olympics.com/en/paris-2024/schedule/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    print("Title:", soup.title.string)

    for link in soup.find_all('a'):
        print("Link:", link.get('href'))

with open('requirements.txt', 'r') as file:
    file_content = file.read()  
    pattern = r"^#!/.*python3?$"

    match = re.search(pattern, file_content)

    if match:
        print("Pattern found in main.py")
    else:
        print("Pattern not found in main.py") 