#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/5/11 19:52
# @File    : functions.py
# @Software: PyCharm

import time
import string
import random
import logging
import uuid
import yaml
from bs4 import BeautifulSoup
from datetime import datetime


# 生成随机9位数字字母码
def generateState():
    return ''.join(random.sample(string.digits + string.ascii_letters, 19))


def get_t():
    return int(datetime.utcnow().timestamp() * 1000)


def getLT(casResponse):
    soup = BeautifulSoup(casResponse.text, features='lxml')
    try:
        scriptPart = soup.find("script", id="password_template").get_text()
        if scriptPart is not None:
            logging.debug("Find Script OK!")
            realSoup = BeautifulSoup(scriptPart, "lxml")
            try:
                lt = realSoup.find("input", attrs={"type": "hidden", "id": "lt"})['value']
                if lt is not None:
                    logging.debug("Find LT OK!")
                    logging.debug("LT:  {}".format(lt))
                    return lt
            except AttributeError as e:
                logging.error("Find LT Fail! => {}".format(e))
                raise e
    except AttributeError as e:
        logging.error("bs4 Find Script Fail! => {}".format(e))
        raise e


def get_sklTicket():
    return str(uuid.uuid4())


def loadCfg(path):
    data = yaml.load(open(path), Loader=yaml.FullLoader)
    return data


def writeCfg(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(yaml.dump(data, allow_unicode=True, sort_keys=False))
