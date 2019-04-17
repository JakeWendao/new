#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:jakewendao

from selenium import webdriver
import unittest
import sys

class TestLogin(unittest.TestCase):

    def setUpClass(self):
        self.driver = webdriver.Firefox()
    def tearDown(self):
        self.driver.close()
    def test_b(self):
        self.driver.get("http://www.baidu.com")
        title = self.driver.title
        print title
    def test_a(self):
        self.driver.get("http://www.baidu.com")
        title = self.driver.title
        print title*2
if __name__ == '__main__':
    # 需要先对TestSuite进行实例化
    # 注意TestLogin.test_a()也可以用TestLogin("test_a")来表达
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_b"))
    suite.addTest(TestLogin("test_a"))
    # 然后执行这个套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    #这里为什么添加的先后顺序不行？
    #2次提交