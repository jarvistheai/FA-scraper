#!/usr/bin/env python3

from requests_html import HTMLSession
session = HTMLSession()

with open('fa_url.txt', 'r') as file:
    url = file.read().strip()

with open('cookies.txt', 'r') as file:
    f = file.readlines()

cookies = {}
for line in f:
    key, value = line.split()
    cookies[key] = value

r = session.get(url=url, cookies=cookies, timeout=5)


title = r.html.find('title', first=True).text
sidebar = r.html.find('.message-bar-desktop', first=True).text

colleft = r.html.find('.userpage-layout-left-col', first=True)
rwatchers = colleft.find('.userpage-left-column')[3]
watchers = rwatchers.find('.floatright', first=True).text
wnum = watchers.split()[-1].strip(')') + ' watchers total'


print()
print('-'*len(title))
print(title)
print('-'*len(title))
print(' '*int((len(title)- len(sidebar))/2) + sidebar)
print('-'*len(title))
print(' '*int((len(title)- len(wnum))/2) + wnum)
print('-'*len(title))
print()
