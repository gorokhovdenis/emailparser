from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import re
req = Request('https://tokenmarket.net/blockchain/ethereum/assets/vtuur/', headers={'User-Agent': 'Mozilla/5.0'})
page=urlopen(req).read()
soup = BeautifulSoup(page,"html.parser")
#links = []
#for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
#    links.append(link.get('href'))
#link = soup.find("div", {"class":"div.col-xs-12.col-sm-2.col-lg-3.follow-controls.text-center"}).find("a").get("href")
link = soup.find("a", class_="visit-website").get("href")
print (link)
#page-wrapper > div.asset-page-wrapper > div.container > div > div:nth-child(2) > div.col-xs-12.col-sm-2.col-lg-3.follow-controls.text-center
