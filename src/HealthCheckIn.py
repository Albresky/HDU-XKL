#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/9/15 20:49
# @File    : HealthCheckIn.py
# @Software: PyCharm

import json
import logging

from Utils.Params import *
from Utils.functions import gen_skl_ticket
from login import Login


class HealthCheckIn:
    def __init__(self):
        self.login = Login()
        self.param = self.login.skl_login()
        self.url_healthCheck = "https://skl.hdu.edu.cn/api/punch"
        # self.url_healthCheckHistory = "https://skl.hdu.edu.cn/api/punch/my"

    def check(self):
        print("++++++++++++++健康打卡++++++++++++++")
        try:
            preRequest = self.login.session.options(url=self.url_healthCheck, headers=headers_check_option)
            if preRequest.status_code == 200:
                logging.debug("健康打卡OPTION预检成功！")
                print("健康打卡OPTION预检成功！")
            else:
                logging.debug("健康打卡OPTION预检失败！")
                print("健康打卡OPTION预检失败！")
                return
            headers = headers_health_check
            headers["skl-ticket"] = gen_skl_ticket()
            headers["X-Auth-Token"] = self.param[1]
            data = location_params
            response = self.login.session.post(url=self.url_healthCheck, headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                print("健康打卡请求成功[200]！")
                print(response.text)
                return
            else:
                print("健康打卡请求失败[{}]".format(response.status_code))
                print(response.text)
                self.check()
                # return
            logging.debug("连接失败！")

        except Exception as e:
            logging.error(e)


'''请求头增加了sentry-trace，为避免检测，暂时放弃实现打卡列表'''
def getHistory(self):
    pass
    # print("======健康打卡每日记录======")
    # try:
    # req=self.login.session.get(url=self.url_healthCheckHistory)
