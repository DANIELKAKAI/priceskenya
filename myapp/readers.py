
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup



def jumia_reader():
    url_name = "https://www.jumia.co.ke/catalog/?q=tecno+k7"
    req = Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    soup = BeautifulSoup(page_html, 'html.parser')
    containers = soup.find_all("div", class_="sku -gallery -has-offers")
    list = []
    for i in containers:
        a = i.find("img")
        b = i.find_all("span")[6].text  #unreliable
        list.append([a['data-src'], a['alt'], b])
    return list




def masoko_reader():
    url_name = "https://www.masoko.com/catalogsearch/result/?q=tecno+k7"
    req = Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    soup = BeautifulSoup(page_html, 'html.parser')
    containers = soup.find_all("li", class_="item product product-item")
    list = []
    for i in containers:
        a = i.find("img")
        b = i.find_all("span",class_="price")[0].text
        list.append([a['src'], a['alt'], b])
    return list




def kili_reader():
    url_name = "https://www.kilimall.co.ke/?act=search&keyword=tecno+k7"
    req = Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    soup = BeautifulSoup(page_html, 'html.parser')
    containers = soup.find_all("div", class_="goods-content")
    list = []
    for i in containers:
        a = i.find("img")
        b = i.find_all("a",class_="lazyload")[0]['title']
        c = i.find("em").text
        list.append([a['data-src'], b, c])
    return list



