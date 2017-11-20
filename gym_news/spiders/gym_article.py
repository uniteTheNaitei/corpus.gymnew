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
    title = response.xpath("//div[@class='boxContainerDiv']/h3/a/text()").extract()

    content = response.xpath("//div[@class='boxContainerDiv']/ul").extract()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",content)
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", content)
    for x,y in zip(title, content):
        #print(x)
        yield {"title":x, "content":y}
    """body_text = response.css(".body-text")
        for text in body_text:
            text_content = text.css("::text").extract()
            if type(text_content) == list:
                text_content = u"".join(text_content)
            content += text_content + " "

        title = response.css("h1 ::text").extract_first()
        yield {"url": url, "id": id, "title": title, "content": content}
        """
