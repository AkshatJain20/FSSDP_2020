# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:51:40 2020

@author: Akshat jain
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("G:\webdrivers\chromedriver.exe")
browser.get(url)
A = [] 
items = []
qua = []
dep = []
std = []
end = []
k = browser.find_element_by_class_name('bid_no')
k.click()
sleep(5)
box = browser.find_element_by_id("pagi_content")
for division in box.find_elements_by_tag_name('div'):
    bidno = division.find_elements_by_class_name('block_header')
    info = division.find_elements_by_tag_name('span')
    add = division.find_elements_by_class_name('add-height')
    if len(info)==4:
        A.append(bidno[0].text.strip())
        items.append(info[0].text.strip())
        qua.append(info[1].text.strip())
        dep.append(add[0].text.strip())
        std.append(info[2].text.strip())
        end.append(info[3].text.strip())

    
import pandas as pd
df = pd.DataFrame()
df["BID_NO"]=A
df["Item(s)"]=items
df["Quantity req"]=qua
df["Department Name and Address"]=dep
df["Start date"]=std
df["end date"]=end
df.to_csv("bid_plus.csv")

browser.quit()
        
       