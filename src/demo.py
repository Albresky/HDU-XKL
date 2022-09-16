#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/5/13 13:13
# @File    : demo.py
# @Software: PyCharm

import sys,os
sys.path.append(os.getcwd())
from HealthCheckIn import HealthCheckIn
from ClassCheckIn import ClassCheckIn

# 课堂签到
# myCheck = ClassCheckIn()
# myCheck.getUserinfo()  # 获取用户信息
# myCheck.getCourse("2022-09-08")  # 获取开始时间为*的课表
# myCheck.check()                 # 上课啦签到

# 每日健康打卡
myCheck = HealthCheckIn()
myCheck.check()
