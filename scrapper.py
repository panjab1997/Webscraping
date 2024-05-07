from bs4 import BeautifulSoup
import requests

req = requests.get("https://www.geeksforgeeks.org/")

soup = BeautifulSoup(req.content, "html.parser")


print(soup.get_text())