import requests
import json
import logging
import datetime
from collections import namedtuple

NR_PAGES = 6
BASE_URL = 'https://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page='
BASE_FILENAME = 'espn'
BREAKLINE = '\n'

logging.basicConfig(level=logging.INFO, 
                    filename=f'{BASE_FILENAME}_{datetime.datetime.now()}.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':

    News = namedtuple('News', ['author', 'summary'])

    news_list = []

    logging.info('Searching for the news...')

    for page in range(1, NR_PAGES):
        url = f'{BASE_URL}{page}'
        res = requests.get(url, verify=False)
        data = json.loads(res.text)
        
        for news in data:
            news_list.append(News(news['author'], news['summary']))

    
    with open(f'{BASE_FILENAME}_{datetime.datetime.now()}.txt', 'w') as exported_file:
        logging.info('Exporting news to file...')
        for news in news_list:
            exported_file.write(f'{news.summary} ({news.author}){BREAKLINE}')

    logging.info('News processing has finished.')
