
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

emplist = [['','','',''],['','','',''],['','','',''],['','','','']]


def jumia_reader(data):
    url_name = "https://www.jumia.co.ke/catalog/?q="+data
    req = Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    soup = BeautifulSoup(page_html, 'lxml')
    containers = soup.find_all("div", class_="sku -gallery -has-offers")
    list = []
    try:
        for i in containers:
            a = i.find("img")
            b = i.find("span",class_="price").find_next("span",dir="ltr").text
            c = i.find("a")
            list.append([a['data-src'], a['alt'], b,c['href']])
        return list
    except:
        return emplist




def masoko_reader(data):
    url_name = "https://www.masoko.com/catalogsearch/result/?q="+data
    req = Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    soup = BeautifulSoup(page_html, 'lxml')
    containers = soup.find_all("li", class_="item product product-item")
    list = []
    try:
        for i in containers:
            a = i.find("img")
            b = i.find("span",class_="price").text
            c = i.find("a")
            list.append([a['src'], a['alt'], b,c['href']])
        return list
    except:
        return emplist    




def kili_reader(data):
    url_name = "https://www.kilimall.co.ke/?act=search&keyword="+data
    req = Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    soup = BeautifulSoup(page_html, 'lxml')
    containers = soup.find_all("div", class_="goods-content")
    list = []
    try:
        for i in containers:
            a = i.find("img")
            b = i.find("a",class_="lazyload")['title']
            c = i.find("em").text
            d = i.find("a")
            list.append([a['data-src'], b, c,d['href']])
        return list
    except:
        return emplist



def pigia_reader(data):
    url_name = "https://www.pigiame.co.ke/classifieds?q="+data
    req = Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    soup = BeautifulSoup(page_html, 'lxml')
    containers = soup.find_all("div", class_="listings-cards__list-item")
    list = []
    try:       
        for i in containers:
            a = i.find("img")
            b = i.find("span",class_="listing-card__price__value").text
            c = i.find("a")
            list.append([a['src'], a['alt'], b,c['href']])
        return list
    except:
        return emplist




