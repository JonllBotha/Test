import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
URL = "https://olympics.com/en/paris-2024/schedule/"
r = requests.get(URL)
print(r.content)
