#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 23:51:25 2019

@author: manzar
"""

import requests
from bs4 import BeautifulSoup
url = "http://www.vinafruit.com/vinafruit/member.php?lang=1"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
tr = soup.findAll('tr', {'bgcolor': '#FFFFFF'})
count = 0
file = open('assignment.csv', 'w')
header = 'Company Name, Telephone, Email, Website\n'
file.write(header)
for row in tr:
    td = row.findAll('td')
    name = td[1].span.text.replace('\n', '').replace('\r', '')
    try:
        tel = td[3].p.contents[0].text.replace('\n', '').replace('\xa0', '').replace('\r', '').split('Tel:')[1]
    except:
        try:
            tel = td[3].p.contents[0].text.replace('\n', '').replace('\r', '').replace('\xa0', '').split('Tel :')[1]
        except:
            try:
                tel = td[3].p.contents[0].text.replace('\n', '').replace('\r', '').replace('\xa0', '').split('Tel/Fax :')[1]
            except:
                tel = td[3].p.contents[0].text.replace('\n', '').replace('\r', '').replace('\xa0', '').split('Tel/fax :')[1]                
    
    tel = tel.split('Fax')[0].split('HP')[0].replace('\n', '').replace(',', ' | ')
    
    try:
        email = td[4].p.a.attrs['href'].replace('mailto:', '')
    except:
        email = 'NaN'
    
    try:
        web = td[5].p.a.attrs['href'].replace('mailto:', '')
    except:
        web = 'NaN'
    print(name.replace('\n', ''))
    file.write(name.replace(',', '') + ', ' + tel + ', ' + email + ', ' + web + '\n')
    count += 1
    
file.close()