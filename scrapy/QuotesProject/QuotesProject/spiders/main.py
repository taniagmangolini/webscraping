import scrapy

class QuotesSpyder(scrapy.Spider):
    """ 
    This is an example of a scrapy spider inside a scrapy project.
    To run it, execute: 
                        python -m scrapy crawl quotes
    To output the results to a file:
                        python -m scrapy crawl quotes -o results.csv
    """
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):

        print(f'Url {response.url}')
        print(f'Request {response.request}')
        print(f'Meta {response.meta}')
        print(f'Status {response.status}')
        
        print(f'Header {response.headers}')
        print(f'Header Content-Type{response.headers.getlist("Content-Type")}')
        print(f'Header Content-Type{response.headers.get("Content-Type")}')

        print(f'Header Content-Type{response.body.decode("utf-8")}')

        for quote in response.css('div.quote'): # iterate over all div with class quote
            # get() return only the first match. To get all matches, use the getall()
            yield{
                'author': quote.xpath('span/small/text()').get(),
                'author_with_css': quote.css('span small.author::text').get(), # extracts text from spans that have small elements with .author class
                'text': quote.css('span.text::text').get(), # extracts text from span elements with .text class
                'tags': quote.css('a.tag::text').getall(), # extracts text from a  with .tag class
            }
        next_page = response.css('li.next a::attr("href")').get() # next page. Ex. /page/2/

        if next_page is not None:
            print(f'processing page {next_page}...')
            yield(response.follow(next_page, self.parse)) # add to the current url the next page suffix
        else:
            print('The last page was reached.')
