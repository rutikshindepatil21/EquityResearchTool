from datetime import datetime
import schedule
import time
from webScrapper import get_urls
def job():
    urls=get_urls('https://www.moneycontrol.com/news/')
    print(f'scraped links:{len(urls)}')
    with open('daily_news_links.txt','a',encoding='utf-8') as f:
        f.write(f"\n\n-----{datetime.now().date()}-----\n\n")
        for link in urls:
            f.write(link+ '\n')

    print('Saved to daily_news_links.txt ✅')
# schedule.every().day.at("09:00").do(job)
# schedule.every().day.at("12:00").do(job)
# schedule.every().day.at("15:00").do(job)
# schedule.every().day.at("18:00").do(job)
# schedule.every().day.at("21:00").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(60)
