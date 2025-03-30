import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('div', class_='data').text.strip()
        return data
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Example usage:
url = "http://example.com"
print(fetch_and_parse(url))
