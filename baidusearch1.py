#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

from init import Init
import time

class Search(Init):
    def test_search1(self):
        '''测试百度搜索，搜索人名'''
        a = self.driver.find_element_by_id('kw')
        a.send_keys('lilei')
        b = self.driver.find_element_by_id('su')
        b.click()
        #下面这个强制等待时间是有必要的，假如没有这行代码需要出现的内容就不会出现。
        #  在这里self.driver.implicitly_wait(3) 是不能替代sleep的。
        time.sleep(3)
        print self.driver.title
    def test_fail(self):
        '''这是一个故意失败的案例。测试title名称是否正确'''
        x = False
        self.assertTrue(x)