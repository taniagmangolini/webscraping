import requests
from collections import defaultdict
import logging

logging.basicConfig(level=logging.INFO, 
                    filename='webscraping.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

AUTHOR_BEGIN = '<span>by <small class="author" itemprop="author">'
AUTHOR_END = '</small>'
QUOTE_BEGIN = '<span class="text" itemprop="text">“'
QUOTE_END = '”</span>'
URL = 'https://quotes.toscrape.com/'


if __name__ == '__main__':

    quote_author = defaultdict(list)
    try:
        r = requests.get(URL, verify=False)

        logging.info(f'status {r.status_code}')
        logging.info(f'encoding {r.encoding}')

        html = r.text

        quote = None
        for line in html.split('\n'):
            if QUOTE_BEGIN in line:
                line = line.replace(QUOTE_BEGIN, '')
                quote = line.replace(QUOTE_END, '').strip()
                quote_author[quote]

            if AUTHOR_BEGIN in line:
                line = line.replace(AUTHOR_BEGIN, '')
                author = line.replace(AUTHOR_END, '').strip()
                quote_author[quote].append(author)

    except Exception as e:
        logging.info(f'[EXCEPTION] {e}')
