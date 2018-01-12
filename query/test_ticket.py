#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 15:10
# @Author  : huanghe
# @Site    : 
# @File    : test_ticket.py
# @Software: PyCharm
from query.get_ticket import getList


for li in getList():
    ticket = li.split('|')
    print('列车：'+ ticket[3]+'二等座：'+ticket[30]+',软卧：'+ticket[28]+',硬卧：'+ticket[26])