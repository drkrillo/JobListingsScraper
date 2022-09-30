import scrapy

class CraiglistItem(scrapy.Item):
    # Define fields to be scraped
    date = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    job_title = scrapy.Field()
    earnings = scrapy.Field()
    job_type = scrapy.Field()