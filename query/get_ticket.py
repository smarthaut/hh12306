#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 14:53
# @Author  : huanghe
# @Site    : 
# @File    : get_ticket.py
# @Software: PyCharm
from urllib import request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

def getList():
    url = r'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-10&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=SQF&purpose_codes=ADULT'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }

    req = request.Request(url=url, headers=headers)
    page = request.urlopen(req).read().decode('utf-8')
    dict = json.loads(page)
    return dict['data']['result']