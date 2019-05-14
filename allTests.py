#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

import unittest
import os
import HtmlTestRunner

def allTestsCase():
    '''返回所有的测试用例'''
    suite = unittest.defaultTestLoader.discover(
        # 假如这里的start_dir是使用具体的目录比如'C:\Users\Public\Favorites'，就需要把反斜杠变为斜杠'C:/Users/Public/Favorites'
        start_dir=os.path.dirname(__file__),
        pattern='new*.py',
        top_level_dir=None
    )
    return suite

def run():
    HtmlTestRunner.HTMLTestRunner()
