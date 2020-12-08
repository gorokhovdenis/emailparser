#!/usr/bin/python3.6
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import re
url=input('Enter url: ')
req = Request(url, headers={'User-Agent': 'Mozilla/62.0'})
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
    with open('/home/mail/base', 'a') as f:
	    f.write(match[i]+'\n')
    i=i+1
with open('/home/mail/base', 'a') as f:
	    f.write('--------\n')
