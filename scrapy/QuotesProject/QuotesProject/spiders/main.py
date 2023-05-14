import scrapy

class QuotesSpyder(scrapy.Spider):
    """ 
    This is an example of a scrapy spider inside a scrapy project.
    To run it, execute: 
                        python -m scrapy crawl quotes
    """
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor',
    ]

    def parse(self, response):

        print(f'Url {response.url}')
        print(f'Status {response.status}')

        print(f'Header {response.headers}')
        print(f'Header Content-Type{response.headers.getlist("Content-Type")}')
        print(f'Header Content-Type{response.headers.get("Content-Type")}')

        print(f'Header Content-Type{response.body.decode("utf-8")}')

        for quote in response.css('div.quote'):
            yield{
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield(response.follow(next_page, self.parse))
