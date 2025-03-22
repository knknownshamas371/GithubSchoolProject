import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h1', class_='example-class')
for title in titles:
    print(title.text)
