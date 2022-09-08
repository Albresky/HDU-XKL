#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/5/13 13:13
# @File    : demo.py
# @Software: PyCharm


from check import Check

myCheck = Check()
myCheck.getUserinfo()           # 获取用户信息
myCheck.getCourse("2022-09-08") # 获取开始时间为*的课表
myCheck.check()                 # 上课啦签到
