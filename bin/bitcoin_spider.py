import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from main import core
import time
from conf.Const import *
import random

def run():
    start_time = time.time()
    runer = core.Core()
    try:
        while True:
            runer.show()
            waitTime = random.randint(REFRESH[0],REFRESH[1])
            time.sleep(waitTime)
            if time.time() - start_time > RUNNING_TIME:
                time.sleep(SLEEPTIME)
                runer.write_file("进入休眠")
                start_time = time.time()

    except Exception as e:
        print("出问题了请检查网络连接!")
        print(e)
        runer.write_file(str(e))
        runer.coincola.browser.close()
        del runer
        run()


run()
