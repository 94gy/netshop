#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gaoyang
# @Date  : 2021/4/23 15:25
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^register/$', views.RegisterView.as_view()),
    url(r'^checkUname/$', views.CheckUnameView.as_view()),
    url(r'^center/$', views.CenterView.as_view())
]