#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao
from selenium import webdriver
import unittest
import sys

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
    def test_login3(self):
        self.driver.get("https://www.v2ex.com/")
        title = self.driver.title
        print title
    def test_login4(self):
        self.driver.get("http://www.baidu.com")
        title = self.driver.title
        print title
def login():
    # 需要先对TestSuite进行实例化
    # 注意TestLogin.test_a()也可以用TestLogin("test_a")来表达
    suite1 = unittest.TestSuite()
    suite1.addTest(TestLogin('test_login4'))
    suite1.addTest(TestLogin('test_login3'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite1)