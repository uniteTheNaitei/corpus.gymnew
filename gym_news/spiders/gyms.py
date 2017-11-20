# -*- coding: utf-8 -*-
import re
from scrapy.spiders import CrawlSpider
import scrapy

from gym_news.spiders.gym_article import GymArticleSpider


class BaomoiSpider(CrawlSpider):
    name = "gym"
    # allowed_domains = ["http://poem.tkaraoke.com/"]
    start_urls = [
        "http://www.total-gym-exercises.com"
    ]
    article_parser = GymArticleSpider()

    def parse(self, response):
        self.logger.info('==> %s', response.url)
        article_pages = response.xpath("//div[@id ='menu2']/ul/li/a/@href").extract()
        for next_page in article_pages:
            yield scrapy.Request(response.urljoin(next_page), callback=self.article_parser.parse)

