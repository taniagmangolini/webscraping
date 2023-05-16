import scrapy


class ImdbSpyder(scrapy.Spider):
    """ 
    This is an example of a scrapy spider inside a scrapy project.
    To run it, execute from inside this project folder: 
                        python -m scrapy crawl imdb
    To output the results to a file:
                        python -m scrapy crawl imdb -o imdb.csv
    """
    name = 'imdb'
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    start_urls = [
        'https://www.imdb.com/chart/top',
    ]

    def parse(self, response):
        for a in response.css('.titleColumn a'):
            url = a.css('::attr("href")').get()
            title = a.css('::text').get()
            meta = {'title': title} # use meta to share data between callbacks
            yield response.follow(url, callback=self.parse_info, meta=meta)

    def parse_info(self, response):
        year = None
        duration = None
        genres = []

        for element in response.css('main[role="main"]'):

            lis = element.css('div.kRUqXl div ul li.ipc-inline-list__item[role="presentation"]')
            span = element.css('div.dDTLMQ div div section div div.ipc-chip-list__scroller a span')

            if span:
                genres = span.css('::text').getall()
            
            if lis:
                for li in lis:
                    if li.xpath('a[contains(@href, "tt_ov_rdat")]'):
                        year = li.css('a[role="button"]::text').get()
                    elif li.css(':last_child'):
                        duration = li.css('::text').get()
            yield {
                'title': response.meta['title'],
                'year': year,
                'duration': duration,
                'genres': genres
            }
