#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gaoyang
# @Date  : 2021/4/8 17:00

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.IndexView.as_view()),
    url(r'^category/(\d+)$', views.IndexView.as_view()),
    url(r'^category/(\d+)/page/(\d+)$', views.IndexView.as_view()),
    url(r'^goodsdetails/(\d+)$', views.DetailView.as_view())
]
