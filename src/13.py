# this is just an example to showcase how you can write code on your github school project.
import os
import requests

def download_file(url, local_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded: {local_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

url = "https://example.com/file.txt"
download_file(url, "./downloads")
