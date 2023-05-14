import requests
from bs4 import BeautifulSoup
import logging
from collections import namedtuple
import re


logging.basicConfig(level=logging.INFO, 
                    filename='imdb.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

URL_BASE = 'https://www.imdb.com'
URL_TOP_MOVIES = f'{URL_BASE}/chart/top'
Movie = namedtuple('Movie', ['id', 'title', 'rating', 
                   'url', 'genres', 'duration', 'year'])


def parse_top_rated_movie_info(tr):
    ''' Extract rated movie id, name, rating and url.
    '''
    column_title = tr.find('td', {'class': 'titleColumn'})

    title = column_title.a.string
    rating = tr.find('td', {'class': 'ratingColumn imdbRating'}).strong.string
    id = column_title.a['href']
    url = f'{URL_BASE}/{id}'

    genres, duration, year = get_top_rated_movie_detail(url)

    return Movie(id, title, rating, url, genres, duration, year)


def get_top_rated_movie_detail_genres(soup):
    ''' Extract genres from movies details page.
    '''
    genres = []
    for genre in soup.findAll('span', {'class': 'ipc-chip__text'}):
        if 'Back to top' not in genre.string:
            genres.append(genre.string)

    return genres


def get_top_rated_movie_detail_year(soup):
    ''' Extract year from movies details page.
    '''
    year = None
    pattern = r'ipc-link.+inherit-color'
    items = soup.findAll('a', {'class': re.compile(pattern),
                             'role': 'button'})
    for item in items:
        if 'tt_ov_rdat' in item['href']:
            year = item.string

    return year


def get_top_rated_movie_detail_duration(soup):
    ''' Extract duration from movies details page.
    '''
    duration = None
    pattern = r'ipc-inline-list.+baseAlt'
    ul_list = soup.findAll('ul', {'class': re.compile(pattern),
                               'role': 'presentation'})
    for ul in ul_list:
        for li in ul:
            if li.a is None:
                duration = li.string

    return duration


def get_top_rated_movie_detail(url):
    ''' Extract year, genre, duration from movie.
    '''  
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                              AppleWebKit/537.36 (KHTML, like Gecko) \
                              Chrome/102.0.0.0 Safari/537.36'
              }
    default_headers = requests.utils.default_headers()
    logging.info(f'updating req. header {default_headers} to {headers}')

    logging.info('getting movie details ...')
    request = requests.get(url, headers=headers, verify=False)

    logging.info('parsing the details soup ....')
    soup = BeautifulSoup(request.text, 'html.parser')

    genres = get_top_rated_movie_detail_genres(soup)
    year = get_top_rated_movie_detail_year(soup)
    duration = get_top_rated_movie_detail_duration(soup)

    return genres, duration, year


def get_top_rated_movies():
    ''' Get the top rated movies from IMDb.
    '''
    movies = []

    logging.info('getting the top rated movies from IMDb ...')
    request = requests.get(URL_TOP_MOVIES, verify=False)

    logging.info('parsing the soup ....')
    soup = BeautifulSoup(request.text, 'html.parser')
    table = soup.findAll('table', {'class': 'chart full-width'})[0]
    table_body = table.findAll('tbody')[0]

    logging.info('parsing the top rated movies info...')
    trs = table_body.findAll('tr')
    for tr in trs:
        movie = parse_top_rated_movie_info(tr)
        movies.append(movie)
        movies_data = f' - {movie.title}; {movie.genres}; {movie.year}; {movie.duration}; {movie.rating}; {movie.url}'
        logging.info(movies_data)

    return movies


if __name__ == '__main__':
    movies = get_top_rated_movies()
    logging.info(f'A total of {len(movies)} movies has been processed.')
