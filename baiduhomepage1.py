#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

import unittest
from init import Init
import sys


class HomePage(Init):
    def test_home1(self):
        title = self.driver.title
        print title

if __name__ == '__main__':
    # 使用加载测试类形成测试套件的方法，来进行运行单元测试用例
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePage)
    unittest.TextTestRunner(verbosity=2).run(suite)