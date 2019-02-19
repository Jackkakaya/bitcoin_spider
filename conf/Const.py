'''配置文件
'''
import sys
import os
# coincola爬取数量(最大为10)
NUM_COINCOLA = 5

# 刷新频率（单位s）

REFRESH = (20,60)

#　多久时间停止一次，防止ip被禁止(单位s:1h=3600s)

RUNNING_TIME = 1800

# 休息时间（单位s）

SLEEPTIME = 240

#　初始设定为每小时休息3分钟
# 文件根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 报警音乐目录
MUSIC_FILE = BASE_DIR + "\\music\\canon.mp3"

# 好友昵称列表

FRIENDS = ['海纳百川', '汇通天下']
