#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

import unittest
from init import Init
import sys

class TestLogin(Init):
    def test_login3(self):
        title = self.driver.title
        print title

# def login():
#     unittest.main(verbosity=2)
#