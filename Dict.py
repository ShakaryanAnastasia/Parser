from bs4 import BeautifulSoup
import requests
class Parser():
    URL = 'https://www.wordreference.com/enru/'
    HEADERS = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36', 'accept': '*/*'}
    HOST = 'https://www.wordreference.com'

    def get_html (self, url, params = None):
        r = requests.get(url, headers = self.HEADERS, params = params)
        return r

    def define(self, word):
        html = self.get_html(self.URL+word)
        if html.status_code == 200:
            html = html.text
            define = {}
            key = 1
            soup = BeautifulSoup(html, 'html.parser')
            items = soup.find_all('tr', id = True)
            for item in items:
                tmps = item.find_all('td')
                tmp = tmps[1].text
                exception = '\xa0'+ tmps[1].find('span', class_ = 'dsense').text
                define[key] = tmp.replace(exception, '')
                key+=1
            return define
        else:
            print ('Error')

    def get_examples(self, word):
        html = self.get_html(self.URL+word)
        if html.status_code == 200:
            html = html.text
            example = {}
            soup = BeautifulSoup(html, 'html.parser')
            items = soup.find_all('td', colspan="2", class_='FrEx')
            for item in range(len(items)):
                example[item+1]=items[item].text
            return example
        else:
            print ('Error')

parse = Parser()
print(parse.define('cat'))
print(parse.get_examples('cat'))

