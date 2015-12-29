#!/usr/bin/env python
# coding: utf-8
__author__ = 'whoami'

"""
@version: 1.0
@author: whoami
@license: Apache Licence 2.0
@contact: skynet@gmail.com
@site: http://www.itweet.cn
@software: PyCharm Community Edition
@file: skynet.py
@time: 2015-12-29 下午4:25
"""

import action_process
import serializer
import pickle

class skynet(object):

    def __init__(self):
        self.hosts = serializer.all_host_configs()

    def handle(self,msg):
        #print 'recv:',msg
        action_process.action_process(self,msg)
        print '---------waiting for new msg ---------'

        #received data
        for host,val in self.hosts['hosts'].items():
            if len(val.keys()) >= 6:
                print host,val

    def forward(self,msg):
        print '-------starting Processing data---------'
        self.handle(msg)

    def process(self):
        pass