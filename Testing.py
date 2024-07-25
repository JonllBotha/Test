import requests 
from bs4 import BeautifulSoup  
URL = "https://olympics.com/en/paris-2024/schedule/"
r = requests.get(URL)
print(r.content)
