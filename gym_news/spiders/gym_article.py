import re
from scrapy.spiders import CrawlSpider
import scrapy


class GymArticleSpider(CrawlSpider):
  name = "gym"
  # allowed_domains = ["http://poem.tkaraoke.com/"]
  start_urls = [
      "www.total-gym-exercises.com/exercises/abs/index.html",
  ]

  def parse(self, response):
    self.logger.info('==> %s', response.url)
    url = response.url
    #id = re.compile(".*/(\d+).epi").match(url).groups()[0]
    title = response.xpath("//h2[@class='ExHeading ExHeading--h2 ExDetail-h2']/text()").extract_first()
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",title)
    content = response.xpath("//li[@class='ExDetail-descriptionStep']/text()").extract()
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",content)
    img_m = response.xpath("//img[@class='ExImg ExDetail-img js-ex-enlarge']/@data-large-photo").extract_first()
    img_l = response.xpath("//img[@class='ExImg ExDetail-img js-ex-enlarge']/@src").extract_first()
    return {"title":title, "content":content, "img":[img_m, img_l]}
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", content)
    #for x,y in zip(title, content):
    #    #print(x)
    #    yield {"title":x, "content":y}
    
