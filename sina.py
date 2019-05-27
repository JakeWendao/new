#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

import unittest
from selenium import webdriver

class sina(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('https://mail.163.com')
    def tearDown(self):
        self.driver.quit()
    def test_unlogin(self):
        self.driver.implicitly_wait(30)
        #通过xpath来寻找动态iframe
        iframe = self.driver.find_element_by_xpath("//iframe[starts-with(@id,'x-URS-iframe')]")
        self.driver.switch_to.frame(iframe)
        #判断按钮是否被选中，并把状态返回给变量un_login
        un_login = self.driver.find_element_by_id('un-login').is_selected()
        self.assertTrue(un_login)
