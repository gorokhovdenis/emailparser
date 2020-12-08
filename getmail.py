#!/usr/bin/python3.6
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import re
url=input('Enter url: ')
req = Request(url, headers={'User-Agent': 'Mozilla/62.0'})
page=urlopen(req).read()
soup = BeautifulSoup(page,"html.parser")
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
