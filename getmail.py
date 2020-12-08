from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import re
def getsite(url):
    #getting the url of website from page which find in def main()
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page=urlopen(req).read()
    soup = BeautifulSoup(page,"html.parser")
    link = soup.find("a", class_="visit-website").get("href")
    getmail(link)

def getmail(sitelink):
    req = Request(sitelink, headers={'User-Agent': 'Mozilla/62.0'})
    time.sleep(2)
    page=urlopen(req).read()
    time.sleep(2)
    soup = BeautifulSoup(page,"html.parser")
    time.sleep(1)
    string = str(page)
    match=(re.findall(r'[\w.-]+@[\w.-]+', string))
    i=0
    while i < len(match):
        print (match[i])
        with open('/home/den/mail/base', 'a') as f:
            f.write(match[i]+'\n')
        i=i+1
    with open('/home/den/mail/base', 'a') as f:
            f.write('--------\n')

def main():
    req = Request('https://tokenmarket.net/ico-calendar/upcoming', headers={'User-Agent': 'Mozilla/5.0'})
    page=urlopen(req).read()
    soup = BeautifulSoup(page,"html.parser")
    links = []
    for link in soup.find_all('a', class_="logo-link"):
        links.append(link.get('href'))
    i=0
    while i < len(links):
        getsite(links[i])
        i=i+1

main()
