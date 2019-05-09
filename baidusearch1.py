#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

from init import Init

class SearchNews(Init):
    def test_search1(self):
        a = self.driver.find_element_by_id('kw')
        a.send_keys('lilei')
        b = self.driver.find_element_by_id('su')
        b.click()
        print self.driver.title