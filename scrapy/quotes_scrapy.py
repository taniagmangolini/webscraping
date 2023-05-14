import scrapy

class QuotesSpyder(scrapy.Spider):
    """ This is an example of a simple scrapy script.
        To run it: scrapy runspider quotes_scrapy.py -o quotes_scrapy.json
        The extracted data will be in the output json file.
    """
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield(response.follow(next_page, self.parse))
