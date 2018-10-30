#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-10-23 下午1:25
# @Author  : Lone
# @Site    : 
# @File    : run_test.py
# @Software: PyCharm

import time
import unittest
from testscript import logger, get_result

logger = logger.Logger(logger="TestRunner").getlog()

class TestVioce(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_get_result_11(self):
        male_result = get_result.GetResult("male", 1000, 1200).get_result()
        time.sleep(5)
        female_result = get_result.GetResult("female", 1000, 1200).get_result()
        print(male_result, female_result)
        self.assertGreaterEqual(male_result, 0.9)
        self.assertGreaterEqual(female_result, 0.9)

    # def test_get_result_37(self):
    #     male_result = get_result.GetResult("male", 1000, 1300).get_result()
    #     female_result = get_result.GetResult("female", 2000, 2700).get_result()
    #     print(male_result, female_result)
    #     self.assertGreaterEqual(male_result, 0.9)
    #     self.assertGreaterEqual(female_result, 0.9)
    #
    # def test_get_result_28(self):
    #     male_result = get_result.GetResult("male", 1000, 1200).get_result()
    #     female_result = get_result.GetResult("female", 2000, 2800).get_result()
    #     print(male_result, female_result)
    #     self.assertGreaterEqual(male_result, 0.9)
    #     self.assertGreaterEqual(female_result, 0.9)
    #
    # def test_get_result_46(self):
    #     male_result = get_result.GetResult("male", 1000, 1400).get_result()
    #     female_result = get_result.GetResult("female", 2000, 2600).get_result()
    #     print(male_result, female_result)
    #     self.assertGreaterEqual(male_result, 0.9)
    #     self.assertGreaterEqual(female_result, 0.9)
    #
    # def test_get_result_64(self):
    #     male_result = get_result.GetResult("male", 1000, 1600).get_result()
    #     female_result = get_result.GetResult("female", 2000, 2400).get_result()
    #     print(male_result, female_result)
    #     self.assertGreaterEqual(male_result, 0.9)
    #     self.assertGreaterEqual(female_result, 0.9)
    #
    # def test_get_result_73(self):
    #     male_result = get_result.GetResult("male", 1000, 1700).get_result()
    #     female_result = get_result.GetResult("female", 2000, 2300).get_result()
    #     print(male_result, female_result)
    #     self.assertGreaterEqual(male_result, 0.9)
    #     self.assertGreaterEqual(female_result, 0.9)
    #
    # def test_get_result_82(self):
    #     male_result = get_result.GetResult("male", 1000, 1800).get_result()
    #     female_result = get_result.GetResult("female", 2000, 2200).get_result()
    #     print(male_result, female_result)
    #     self.assertGreaterEqual(male_result, 0.9)
    #     self.assertGreaterEqual(female_result, 0.9)


if __name__ == '__main__':
    test_result = unittest.main()
    # print(result)