import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler')

soup = BeautifulSoup(html_doc.text, 'html.parser')

popular_area = soup.find(attrs={'class': 'grid-row list-content'})

images = popular_area.findAll(attrs={'class':'media__image'})
titles = popular_area.findAll(attrs={'class':'media__title'})

for image in images:
    print(image.find('a').find('img')['title'])

