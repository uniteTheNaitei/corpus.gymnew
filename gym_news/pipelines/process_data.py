import json
import os
from os.path import dirname
import sys
import re


class Article:
    def __init__(self, data):
        self.__dict__ = data
        self._content_preprocess()
    
    def _content_preprocess(self):
        self.content = re.sub("<[^>]*>", "",self.content)
        self.content = self.content.replace("\t", "")
        self.content = self.content[1:-2]

    def save(self, folder):
        filename = "%s.txt" % self.title
        filepath = os.path.join(folder, filename)
        with open(filepath, "w") as f:
            f.write(self.title+"\n")
            f.write(self.content)

if __name__ == '__main__':
    folder = dirname(dirname(sys.argv[0]))
    data_folder = os.path.join(folder, "data")
    js_files = os.path.join(folder, "raw_data", "data.jl")
    lines = open(js_files).readlines()
    articles = [Article(json.loads(line)) for line in lines]
    indexed_files = os.listdir(os.path.join(folder, "data"))
    indexed_articles = [f.split(".")[0] for f in indexed_files]
    new_articles = [article for article in articles if article.title not in indexed_articles]
    for article in new_articles:
        print("New article %s" % article.title)
        article.save(data_folder)
    print("Indexed articles: %s" % len(indexed_articles))
    print("Crawled articles: %s" % len(articles))
    print("New articles    : %s" % len(new_articles))
