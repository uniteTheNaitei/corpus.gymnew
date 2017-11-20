python gym_news/pipelines/pre_crawl.py
scrapy runspider gym_news/spiders/bgym.py -o gym_news/raw_data/data.jl -t jsonlines --set HTTPCACHE_ENABLED=0
python gym_news/pipelines/process_data.py
git add -A
git commit -m "update data"
git push origin master
