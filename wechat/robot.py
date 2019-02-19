'''
    author:jack
    date:2018-02-11 10:00
    interface by wechat
'''
from wxpy import *
from conf.Const import *


class Robot():
    def __init__(self):
        self.bot = Bot(cache_path=True)
        self.friends = list(map(self.bot.search, FRIENDS))

    def sendMessage(self, content):
        friends = (friend[0].send(content) for friend in self.friends)
        list(friends)
