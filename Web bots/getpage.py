from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.google.com')
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)

