#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/5/11 19:52
# @File    : functions.py
# @Software: PyCharm

import logging
import random
import secrets
import string
import uuid
from datetime import datetime

import yaml
from bs4 import BeautifulSoup


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
    # ToDo
    return str(uuid.uuid4())


def getRandomValues():
    return [secrets.randbits(8) for i in range(21)]


def str36(number):
    num_str = '0123456789abcdefghijklmnopqrstuvwxyz'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append(num_str[i])
    return ''.join(reversed(base36))


def gen_skl_ticket():
    e = ''
    l = getRandomValues()
    for r in l:
        r &= 63
        if r < 36:
            e += str36(r)
        elif r < 62:
            e += str36(r - 26).upper()
        elif r > 62:
            e += '-'
        else:
            e += '_'
    return e


def loadCfg(path):
    data = yaml.load(open(path), Loader=yaml.FullLoader)
    return data


def writeCfg(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(yaml.dump(data, allow_unicode=True, sort_keys=False))


def time2now(thisDate: str):
    nowTime = datetime.now()
    pastDate = datetime.strptime(thisDate, "%Y-%m-%d %H:%M:%S")
    res = nowTime - pastDate
    return res.days * 24 + res.seconds / 3600.0
