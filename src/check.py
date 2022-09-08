#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/5/12 15:22
# @File    : check.py
# @Software: PyCharm

import logging
from login import Login
from Utils.functions import get_t, gen_skl_ticket
from Utils.myHeaders import *


class Check:
    def __init__(self):
        self.login = Login()
        self.param = self.login.skl_login()
        self.url_check = ""
        self.url_course = "https://skl.hdu.edu.cn/api/course?startTime="
        self.url_userinfo = "https://skl.hdu.edu.cn/api/userinfo?type="

    def check(self):
        print("======签到======")
        code = input("请输入签到码:")
        self.url_check = "https://skl.hdu.edu.cn/api/checkIn/code-check-in?userid=" + self.param[0] + "&code=" + str(
            code) + "&latitude=0&longitude=0&t=" + str(get_t())
        try:
            preRequest = self.login.session.options(url=self.url_userinfo, headers=headers_check_option)
            if preRequest.status_code == 200:
                logging.debug("签到OPTION预检成功！")
                print("签到OPTION预检成功！")
            else:
                logging.debug("签到OPTION预检失败！")
                print("签到OPTION预检失败！")
                return
            headers = headers_check_get
            headers["skl-ticket"] = gen_skl_ticket()
            headers["X-Auth-Token"] = self.param[1]
            response = self.login.session.get(url=self.url_check, headers=headers)
            if response.status_code == 200:
                print("签到请求成功[200]！")
                print(response.text)
                return
            elif response.status_code == 401:
                print("签到请求失败[401]！")
                print(response.text)
                self.check()
                # return
            logging.debug("连接失败！")

        except Exception as e:
            logging.error(e)

    def getCourse(self, startDate):
        url = self.url_course + startDate
        headers = headers_check_get
        headers["skl-ticket"] = gen_skl_ticket()
        headers["X-Auth-Token"] = self.param[-1]
        try:
            response = self.login.session.get(url=url, headers=headers)
            logging.info(response.status_code)
            if response.status_code != 200:
                logging.error("请求课表失败")
                return
            logging.debug("请求课表成功")
            print("======课表======\n" + response.text)

        except Exception as e:
            logging.error(e)

    def getUserinfo(self):
        headers = headers_check_get
        headers["skl-ticket"] = gen_skl_ticket()
        headers["X-Auth-Token"] = self.param[-1]
        try:
            response = self.login.session.get(url=self.url_userinfo, headers=headers)
            if response.status_code != 200:
                logging.error("请求课表失败")
                return
            print("======个人信息======\n" + response.text)

        except Exception as e:
            logging.error(e)
