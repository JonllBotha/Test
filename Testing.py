import requests
from bs4 import BeautifulSoup

url = 'https://olympics.com/en/paris-2024/schedule/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print("Title:", soup.title.string)

for link in soup.find_all('a'):
    print("Link:", link.get('href'))

