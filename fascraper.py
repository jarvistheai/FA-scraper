#!/usr/bin/env python3

import os
os.system('clear')
os.chdir('/Users/jarvis/coding/python/FA-scraper/')

import time, datetime
from memfunc import storedata, getdata
from strippers import stripper, destripper
from requests_html import HTMLSession
session = HTMLSession()

# getting the url loaded
with open('fa_url.txt', 'r') as file:
    url = file.read().strip()

# getting the cookies loaded
with open('cookies.txt', 'r') as file:
    cookies = {}
    for line in file:
        key, value = line.split()
        cookies[key] = value

r = session.get(url=url, cookies=cookies, timeout=5)

title = r.html.find('title', first=True).text
sidebar = r.html.find('.message-bar-desktop', first=True).text

colleft = r.html.find('.userpage-layout-left-col', first=True)
rwatchers = colleft.find('.userpage-left-column')[3]
watchers = rwatchers.find('.floatright', first=True).text
wnumraw = watchers.split()[-1].strip(')')
wnum = wnumraw + ' watchers total'

updatestring =  'updates since last pull'
timestampraw = datetime.datetime.now()
timestamp = f"last update {timestampraw.strftime('%Y-%m-%d %I:%M%p')}"

if os.path.exists('memory.txt'):
    msgs = getdata()[0]
    pmsgs = stripper(msgs)
storedata(sidebar)

cmsgs = stripper(sidebar)
newmsgslist = []
for i in range(len(cmsgs)):
    newmsgslist.append(cmsgs[i] - pmsgs[i])
newmsgs = ' '.join(map(str, destripper(newmsgslist)))

os.system('clear')
# print title
print('\n' + '-'*len(title))
print(title)

# print sidebar
if any(c.isdigit()for c in sidebar):
    print('-'*len(title))
    print(' '*int((len(title)- len(sidebar))/2) + sidebar)

# print memory of msgs if something new
if any(c.isdigit()for c in newmsgs):
    print('-'*len(title))
    print(' '*int((len(title)- len(newmsgs))/2) + newmsgs)
    print(' '*int((len(title)- len(updatestring))/2) + updatestring)

# print total watchers
print('-'*len(title))
print(' '*int((len(title)- len(wnum))/2) + wnum)

# print timestamp
print('-'*len(title))
print(' '*int((len(title)- len(timestamp))/2) + timestamp + '\n\n')
