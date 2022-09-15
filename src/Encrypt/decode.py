#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/5/12 16:01
# @File    : decode.py
# @Software: PyCharm


import logging
import js2py


def cacuRsa(userid, password, lt):
    try:
        with open('Encrypt/des.js', 'r', encoding='UTF-8') as f:
            js_code = f.read()
    except FileNotFoundError as e:
        logging.error("des.js not found")
        raise e
    jsFunction = js2py.EvalJs()
    jsFunction.execute(js_code)
    value = userid + password + lt
    _rsa = jsFunction.strEnc(value, '1', '2', '3')
    logging.debug("Compute rsa OK!")
    logging.debug("rsa:  {}".format(_rsa))
    return _rsa
