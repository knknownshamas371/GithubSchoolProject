import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

url = "https://www.example.com"
html_content = fetch_html(url)
if html_content is not None:
    soup = BeautifulSoup(html_content, 'html.parser')
    article_list = soup.find_all('div', class_='article')
    for article in article_list:
        title = article.find('h2').text
        author = article.find('span', class_='author-name').text
        print(f"Title: {title}, Author: {author}")
