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
    def test_spnUid(self):
        self.driver.implicitly_wait(30)
        # spnUid = self.driver.find_element_by_id('spnUid')
        # self.assertEqual(spnUid,'liujingjieyear@163.com')
        # un_login = self.driver.find_element_by_xpath('//*[@id="un-login"]').is_selected()
        #
        # self.driver.find_element_by_tag_name()
        # self.assertFalse(un_login)
        #通过xpath来寻找iframe
        frame = self.driver.find_element_by_xpath("//div[@class='loginUrs']/iframe")
        print frame.id
        # self.driver.switch_to.frame(frame)
        # https://www.cnblogs.com/glre09/p/3231782.html
        #
