import requests
from bs4 import BeautifulSoup
import os

def download_code(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    code_tags = soup.find_all('code', class_='language-python')
    for tag in code_tags:
        file_name = tag.parent.name + '_' + tag.name + '.py'
        with open(file_name, 'w') as f:
            f.write(tag.get_text())

url = "https://www.example.com"  # Replace with the actual URL
download_code(url)
