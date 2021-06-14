from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
from urllib.error import HTTPError
from urllib.error import URLError

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://ja.wikipedia.org{}'.format(articleUrl))
    
    bs =BeautifulSoup(html,'html.parser')
    print(bs.h1.get_text())
    print(bs.find(id = 'mw-content-text').find_all('p')[0])
    if articleUrl == b:
            print('到達')    
    else:
        print('\n')
        return bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))
print('http://ja.wikipedia.orgに続くURLを貼ってください')
a=input('初めのURL>http://ja.wikipedia.org')
b=input('終わりのURL>http://ja.wikipedia.org')
try:
    links = getLinks(a)
    while len(links) > 0:
        newArticle = links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
    