#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 13:34
# @Author  : huanghe
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]