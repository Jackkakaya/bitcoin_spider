'''
    author:jack
    date:2018-02-11 10:00
    公式导入
'''

import json
import os
import hashlib


class Conf(object):
    baseDir = os.path.dirname(os.path.abspath(__file__))

    @classmethod
    def getMd5(self):
        with open(Conf.baseDir + '/conf.json', 'r') as fp:
            md5 = hashlib.md5()
            md5.update(fp.read().encode('utf8'))
            return md5.hexdigest()

    @classmethod
    def isUpdate(self, beforeMd5):
        currentMd5 = Conf.getMd5()
        if beforeMd5 != currentMd5:
            return True
        return False

    @classmethod
    def getConf(self):
        with open(Conf.baseDir + '/conf.json', 'r') as fp:
            return json.load(fp)
