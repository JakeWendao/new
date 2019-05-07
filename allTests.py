#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:jakewendao

import unittest
import os

def allTestsCase():
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.dirname(__file__),
        pattern='new*.py',
        top_level_dir=None
    )
    unittest.TextTestRunner(verbosity=2).run(suite)

allTestsCase()