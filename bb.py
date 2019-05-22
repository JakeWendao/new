#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

import os

print os.getcwd()
case_path = os.path.join(os.getcwd(), "case")
print case_path
report_path = os.path.join(case_path, "case.htm")
print report_path
