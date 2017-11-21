# -*- coding: utf-8 -*-
import re
from scrapy.spiders import CrawlSpider
import scrapy

from gym_news.spiders.gym_article import GymArticleSpider


class BaomoiSpider(CrawlSpider):
    name = "gym"
    # allowed_domains = ["http://poem.tkaraoke.com/"]
    start_urls = [
        #"http://www.total-gym-exercises.com"
        "https://www.bodybuilding.com/exercises/finder/" + str(x) + "/" for x in range(1,73)
    ]
    article_parser = GymArticleSpider()

    def parse(self, response):
        self.logger.info('==> %s', response.url)
        article_pages = response.xpath("//h3[@class ='ExHeading ExResult-resultsHeading']/a/@href").extract()
        print("ajdkhfkjdasfadshfakldnflka", article_pages)
        for next_page in article_pages:
            yield scrapy.Request(response.urljoin(next_page), callback=self.article_parser.parse)

