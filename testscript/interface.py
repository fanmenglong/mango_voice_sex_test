#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-10-23 上午9:31
# @Author  : Lone
# @Site    : 
# @File    : interface.py
# @Software: PyCharm

import requests
import time
from testscript import logger

logger = logger.Logger(logger="InterFace").getlog()

class InterFace(object):
    def __init__(self):
        self.url = "http://134.175.166.135:8080/slot/voice-sex/recognize.do?" \
                   "token=f27fdc05694b645686f55b691f015ef1&flow_id=982eee56c6cc" \
                   "9fda36c823e58692d974&user_id=6419796842174746636"
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

    def get_res(self, file):
        print(file)
        with open(file, "rb") as f:
            files = {"file": f}
            requests.adapters.DEFAULT_RETRIES = 15
            s = requests.session()
            s.keep_alive = False
            # time.sleep(6)
            r = requests.post(self.url, files=files, timeout=50, verify=False, headers=self.headers)
            print("--------------%d" % r.status_code)
            # logger.info("请求返回码为 %d" % r.status_code)
            res = r.json()
            r.close()
            return res
