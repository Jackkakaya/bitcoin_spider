'''
    author:jack
    date:2018-02-11 10:00
    get the price of bitcoin from coincola
'''
from selenium import webdriver
import re
from conf.Const import *


class Coincola():
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)

    @property
    def getPriceList(self):
        self.browser.get('https://www.coincola.com')
        self.browser.find_element_by_link_text("场外交易").click()
        prices = self.browser.find_elements_by_class_name(
            '_3bANGgtfIrZPGW3oO-iGha')[0:5]
        price_list = []
        for price in prices:
            price_list.append(
                float(re.search(r'\d+.?\d+', price.text).group()))
        return price_list

    def __del__(self):
        self.browser.close()
