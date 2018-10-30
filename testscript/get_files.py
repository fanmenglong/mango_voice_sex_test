#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-10-23 上午9:31
# @Author  : Lone
# @Site    : 
# @File    : get_files.py
# @Software: PyCharm

import os.path
from testscript import logger

logger = logger.Logger(logger="GetFiles").getlog()

class GetFiles(object):
    def __init__(self, sex):
        self.path = os.path.dirname(os.path.abspath(".")) + "/testdata/" + sex + "/"
        #self.female_path = os.path.dirname(os.path.abspath(".")) + "/testdata/female/"

    def get_files(self, start_num=0, end_num=5800):
        files = [f for f in os.listdir(self.path) if os.path.isfile(self.path + f)]
        #female_files = [f for f in os.listdir(self.female_path) if os.path.isfile(self.female_path + f)]
        num = end_num - start_num
        if num <= len(files):
            logger.info("获取需要数量的测试样本, 样本数为 %d" % num)
            logger.info("测试样本切片[%d:%d]" % (start_num, end_num))
            return files[start_num:end_num]
        logger.debug("准备样本小于需要数量, 当前总样本数 %d" % (len(files)))
        return files

