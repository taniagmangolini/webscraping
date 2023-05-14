import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO, 
                    filename='webscraping_bs4.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

URL = 'https://quotes.toscrape.com/'


if __name__ == '__main__':
    r = requests.get(URL, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')

    print(soup.title.string)
    print(soup.title.parent.name)

    # search tag span having some attributes
    for tag in soup.findAll('span', {'class': 'text'}):
        print('available attributes:', tag.attrs)
        print(tag.string)

