#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/5/12 16:01
# @File    : decode.py
# @Software: PyCharm


import logging

from Encrypt.des import strEnc


def cacuRsa(userid, password, lt):
    value = userid + password + lt
    _rsa = strEnc(value, '1', '2', '3')
    logging.debug("Compute rsa OK!")
    logging.debug("rsa:  {}".format(_rsa))
    return _rsa

