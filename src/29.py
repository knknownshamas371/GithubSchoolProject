import requests
import os

url = "https://api.github.com/users/lemon-chef/repos"
response = requests.get(url)
repos = response.json()

for repo in repos:
    if repo["name"] == "lunchy":
        print("Found an issue:", repo["message"])
