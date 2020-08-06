from bs4 import BeautifulSoup
import requests
from datetime import datetime
class Parser():
    URL = 'https://store.playstation.com/ru-ru/grid/STORE-MSF75508-GAMEGENREFIGHTIN/1'
    HEADERS = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36', 'accept': '*/*'}
    HOST = 'https://store.playstation.com'

    def parse (self):
        html = self.get_html (self.URL)
        if html.status_code == 200:
            return (self.get_content(html.text))
        else:
            print ('Error')
    def get_html (self, url, params = None):
        r = requests.get(url, headers = self.HEADERS, params = params)
        return r

    def get_content(self, html):
        links = []
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('a', class_='grid-cell__link internal-app-link ember-view')
        for item in items:
            link = item['href']

            link = self.HOST + link
            links.append(link)
        return links
    def get_gb(self):
        links = self.parse()
        print(links)
        list = []
        for link in links:
            html = self.get_html(link)
            ht = html.text
            soup = BeautifulSoup(ht, 'html.parser')
            try:
                item = soup.find('span',{'class':'info-header__detail-item info-header__detail-item--file-size'}).text
            except:
                item = None
            list.append(item)
        print(list)

parse = Parser()
start_time = datetime.now()
parse.get_gb()
finish_time = datetime.now()
print(f'Затраченное время {finish_time-start_time}')