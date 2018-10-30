#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-10-23 上午10:55
# @Author  : Lone
# @Site    : 
# @File    : get_result.py
# @Software: PyCharm

from testscript import get_files, logger, interface
import os.path
import time

logger = logger.Logger(logger="GetResult").getlog()

class GetResult(object):
    def __init__(self, sex, start_num=0, end_num=5800):
        self.sex = sex
        self.path = os.path.dirname(os.path.abspath(".")) + "/testdata/" + sex + "/"
        self.start_num = start_num
        self.end_num = end_num
        #self.female_num = female_num

    def get_right_cnt(self, files):
        right_cnt = 0
        for file in files:
            # time.sleep(2)
            res = interface.InterFace().get_res(self.path + file)
            if res["data"] == self.sex:
                right_cnt += 1
            else:
                print(self.sex + "识别错误")
        return right_cnt

    # def get_right_cnt(self, files):
    #     right_cnt = 0
    #     testfiles = []
    #     cnt = 0
    #     for file in files:
    #         # time.sleep(2)
    #         testfiles.append(file)
    #         cnt += 1
    #         if cnt == 1000:
    #             cnt = 0
    #             for testfile in testfiles:
    #                 res = interface.InterFace().get_res(self.path + file)
    #                 testfiles.remove(testfile)
    #                 if res["data"] == self.sex:
    #                     right_cnt += 1
    #                 else:
    #                     print(self.sex + "识别错误")
    #     return right_cnt

    def get_result(self):
        files = get_files.GetFiles(self.sex).get_files(self.start_num, self.end_num)
        right_cnt = self.get_right_cnt(files)
        result = right_cnt / (self.end_num - self.start_num)
        logger.info("%s测试样本为 %d" % (self.sex, self.end_num - self.start_num))
        logger.info("%s识别正确率为 %.4f" % (self.sex, result))
        return result

