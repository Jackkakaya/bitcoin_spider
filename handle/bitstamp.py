'''
	author:jack
	date:2018-02-11 10:00
	get the price of bitcoin from bitstamp
'''
import requests
import json


class Bitstamp():
    @property
    def lastPrice(self):
        '''
                获取最新价钱

        '''
        response = requests.get('https://www.bitstamp.net/api/ticker/')
        priceDict = json.loads(response.text)
        return float(priceDict['last'])

    @property
    def highPrice(self):
        '''
        　　　获取过去24h内最高价格
        '''
        response = requests.get('https://www.bitstamp.net/api/ticker/')
        priceDict = json.loads(response.text)
        return float(priceDict['high'])

    @property
    def lowPrice(self):
        '''
        　　　获取过去24h内最低价格
        '''
        response = requests.get('https://www.bitstamp.net/api/ticker/')
        priceDict = json.loads(response.text)
        return float(priceDict['low'])
