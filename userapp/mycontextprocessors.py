#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gaoyang
# @Date  : 2021/4/25 13:37
#全局上下文

def getUserInfo(request):
    return {'suser':request.session.get('user', None)}