# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:25:47 2019

@author: Administrator
"""

import requests
import re
import time
import datetime
from csv import writer
import csv

url = "https://steamcommunity.com/market/listings/570/Silent%20Wake"
url_name = "Silent Wake"
html = requests.get(url)
html_bytes = html.content
html_str = html_bytes.decode()

meta_target = "var line1=(\[\[.*?\]\])"
result = re.findall(meta_target, html_str, re.S)[0]
line1 = eval(result.replace("\"","\'"))
datadict = {};
header = ["date","price","count"];
date=[];price=[];count=[];
for i in line1:
    datestr = re.findall("(.*?): \+0",i[0])[0] # 将日期中的时区信息除去，原格式为[%b $d %Y %H]
    dateobj = datetime.datetime.strptime(datestr, "%b %d %Y %H")
    date.append(dateobj)
    price.append(i[1])
    count.append(i[2])
datadict = dict(zip(header,[date, price, count]))



