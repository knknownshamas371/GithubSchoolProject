import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to load URL: {url}")
        return None

def extract_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = soup.find('div', {'class': 'data'}).find_all('p')
    results = []
    for item in data:
        results.append(item.text.strip())
    return results

url = "https://example.com"  # Replace with the desired URL
page_content = fetch_page(url)
if page_content:
    print("Page content fetched successfully.")
    results = extract_data(page_content)
    print("\n".join(results))
else:
    print("Failed to load the page.")
