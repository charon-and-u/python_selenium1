#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest
class xihuanBanGong(unittest.TestCase):
    """
    西环办公
    """

    def setup(self):
        """
        测试固件的setup代码，主要做测试的前提准备
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('')
