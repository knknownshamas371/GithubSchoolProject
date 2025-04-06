import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        raise Exception(f"Failed to get HTML: {response.status_code}")

# Example usage
url = "https://www.example.com"
soup = fetch_html(url)
