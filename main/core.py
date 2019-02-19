from conf import conf
from handle import bitstamp, coincola
import datetime
import re
from wechat.robot import *
from handle import report
from conf.Const import *
import sys


class Core():
    def __init__(self):
        self.bitstamp = bitstamp.Bitstamp()
        self.coincola = coincola.Coincola()
        self.conf = conf.Conf()
        self.function = self.conf.getConf()['function']
        self.threshold = self.conf.getConf()['threshold']
        self.lowThreshold = self.conf.getConf()['lowThreshold']
        self.beforeMd5 = conf.Conf.getMd5()
        self.bot = Robot()

    def show(self):
        MESSAGE = str(datetime.datetime.now()) + "\n"
        coincolaPrices = self.coincola.getPriceList
        bitstamp_price = self.bitstamp.lastPrice
        if(self.conf.isUpdate(self.beforeMd5)):
            self.beforeMd5 = conf.Conf.getMd5()
            self.function = self.conf.getConf()['function']
            self.threshold = self.conf.getConf()['threshold']
            MESSAGE += '********************公式更新了*********************\n'
        MESSAGE += "bitstamp:\t\tCoincola:\t\tDiff\n"
        MESSAGE += str(bitstamp_price) + " USD"
        flag = False
        for index, price in enumerate(coincolaPrices):
            function = re.sub('bitstamp', str(bitstamp_price), self.function)
            function = re.sub('coincola', str(price), function)
            if(index == 0):
                MESSAGE += "\t\t" + str(price) + " CNY"
            else:
                MESSAGE += "\t\t\t" + str(price) + " CNY"
            diff = round(eval(function), 2)
            if (diff > self.threshold or diff < self.lowThreshold):
                MESSAGE += "\t\t" + str(diff)
                MESSAGE += "  here\n"
                flag = True
            else:
                MESSAGE += "\t\t" + str(diff) + "\n"
        if flag:
            report.report(MUSIC_FILE)
            self.bot.sendMessage(MESSAGE)
        MESSAGE += '----------------------------------------------------------\n'
        # self.bot.sendMessage(MESSAGE)
        self.write_file(str(datetime.datetime.now()))
        sys.stdout.write(MESSAGE)
        sys.stdout.flush()

    def write_file(self, content):
        with open('./log', 'a') as f:
            f.write(content + "\n")

    def __del__(self):
        del self.bitstamp
        del self.coincola
        del self.conf
