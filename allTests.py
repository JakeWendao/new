#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

import unittest
import os
import HTMLTestRunner
import baidusearch1
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def allTestsCase():
    '''返回所有的测试用例'''
    suite = unittest.defaultTestLoader.discover(
        # 假如这里的start_dir是使用具体的目录比如'C:\Users\Public\Favorites'，就需要把反斜杠变为斜杠'C:/Users/Public/Favorites'
        start_dir=os.path.dirname(__file__),
        pattern='baidu*.py',
        top_level_dir=None
    )
    return suite

fp = open('TestReport.html','wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                    verbosity=2,
                                    title=u'百度例子测试报告',
                                    description=u'你好，我是描述')
runner.run(allTestsCase())
fp.close()
