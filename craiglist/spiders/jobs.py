import scrapy
from craiglist.items import CraiglistItem
from craiglist.helpers import parsing_chars

class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ['costarica.craigslist.org']
    start_urls = [
            'https://costarica.craigslist.org/search/jjj',
         ]

    def parse(self, response):
        """
        Gathers date, title and url of each listing.
        
        @url https://costarica.craigslist.org/search/jjj
        @returns requests 0 121
        @returns items 0 121
        """
        listings = response.xpath('//li[@class="result-row"]')
        for listing in listings:
            item = CraiglistItem()
            item['date'] = listing.xpath('.//*[@class="result-date"]/@datetime').extract_first()
            item['link'] = listing.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
            item['text'] = listing.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()
            request = scrapy.Request(url=item['link'],
                                     callback=self.parse_listing,
                                    )
            request.meta['item'] = item
            yield request
        
        next_page_url = response.xpath('//*[@class="button next"]/@href').extract_first()

        if next_page_url is not None:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)
    
    def parse_listing(self, response):
        """
        Gathers description, expectation, job type and job title.
        """
        item = response.meta['item']
        item['title'] = response.xpath('.//*[@id="titletextonly"]/text()').extract_first()
        item['description'] = response.xpath('.//section[@id="postingbody"]/text()').extract()
        chars = response.xpath('.//*[@class="attrgroup"]').extract()[0]
        job_title, earnings, job_type = parsing_chars(chars)
        item['job_title'] = job_title
        item['earnings'] = earnings
        item['job_type'] = job_type
        yield item