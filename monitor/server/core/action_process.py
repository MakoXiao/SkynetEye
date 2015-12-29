#!/usr/bin/env python
# coding: utf-8
__author__ = 'whoami'

"""
@version: 1.0
@author: whoami
@license: Apache Licence 2.0
@contact: skutil@gmail.com
@site: http://www.itweet.cn
@software: PyCharm Community Edition
@file: action_process.py
@time: 2015-11-28 下午3:06
"""

import pickle
import serializer

def action_process(server_instance,msg):

    print '>> process data:: %s' % pickle.loads(msg)

    msg = pickle.loads(msg[2])
    # print msg

    func_name = msg.keys()[0]
    func = getattr(serializer,func_name)

    func(server_instance,msg[func_name])