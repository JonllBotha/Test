import requests 
from bs4 import BeautifulSoup  
URL = "https://olympics.com/en/paris-2024/schedule/" ; {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
r = requests.get(URL)
print(r.content)
