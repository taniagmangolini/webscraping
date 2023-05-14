
# Beautiful Soup (BS4)

Bs4 is paired with an HTTP client (for instance requests) to download pages as it can only parse pages.

```
pip3 install bs4
```

# Scrapy 

Scrapy is a full web scraping framework - capable of downloading and parsing pages. 
It also allows to make requests in a parallel and assynchronous way.

It is better for HTML complex structures as it supports XPath Selectors (XML Path Language).

```
pip install scrapy
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



