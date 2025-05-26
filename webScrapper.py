import requests
from bs4 import BeautifulSoup

def get_urls(site_name:str):
    urls=[]
    response=requests.get(site_name)
    html_page=BeautifulSoup(response.text,'lxml')
    tag_page=html_page.find_all('a',href=True)
    for url in tag_page:
        href=url['href']
        if href.startswith('http' ) and "moneycontrol" and 'news' and 'business' in href and not any(x in href for x in ['login', 'register', 'javascript', '#','gamechangers']):
         urls.append(href)
    return list(set(urls))
get_urls('https://www.moneycontrol.com/')



