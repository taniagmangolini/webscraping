
# Beautiful Soup (BS4)

Bs4 is paired with an HTTP client (for instance requests) to download pages as it can only parse pages.

```
pip3 install bs4
```

# Scrapy 

Scrapy is a full web scraping framework - capable of downloading and parsing pages. 
It also allows to make requests in a parallel and in an assynchronous way.

It is better for HTML complex structures as it supports XPath Selectors (XML Path Language. Ex. response.xpath(x_path_selector)) as well css selectors (response.css(css_selector).getall())

```
pip install scrapy
```

## Scrapy Shell

The scrapy has a shell for debug that can be accessed by the following command:

```
python -m scrapy shell
```

You can use this shell to make requests (fetch(url)) and inspect the response (variable response), test selectors and much more!

Example:

```
fetch('http://quotes.toscrape.com/tag/humor')
response.body
fetch('http://quotes.toscrape.com/tag/humor')
```

## Scrapy Script

If you just would like to run a simple scrapy script run:

```
scrapy runspider script.py -o output.json
```
The are many output types supported (json, jsonlines, jl, csv, xml, marshal, pickle).

There are many types of spiders (https://docs.scrapy.org/en/latest/topics/spiders.html). 
Some examples: 

- Spider (the simplest one)

- CrawlSpider (the most commonly used spider for crawling regular websites)

- XMLFeedSpider

- CSVFeedSpider

- SitemapSpider


## Scrapy Project

For more complex cases you can start a new Scrapy project:

```
python  -m scrapy startproject ProjectName
```

For instance: python  -m scrapy startproject QuotesProject


# Selenium

Automates web browser interaction.
Selenium uses a browser web driver (https://www.selenium.dev/pt-br/documentation/webdriver/getting_started/install_drivers).
It is not a specific lib designed for webscraping but can be useful because it supports css selectors and also xpath (https://selenium-python.readthedocs.io/locating-elements.html)

```
pip3 install -U selenium
pip3 install webdriver-manager
```






