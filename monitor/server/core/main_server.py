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
@file: main_server.py
@time: 2015-11-28 下午3:04
"""

from redishelper import RedisHelper
import serializer

import action_process

class MonitorServer(object):

    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.hosts = serializer.all_host_configs()
        self.redis = RedisHelper()

    def handle(self):
        redis_sub = self.redis.subscribe()
        while True:
            msg = redis_sub.parse_response()
            #print 'recv:',msg
            action_process.action_process(self,msg)
            print '---------waiting for new msg ---------'

            #received data
            for host,val in self.hosts['hosts'].items():
                if len(val.keys()) >= 6:
                    print host,val

    def run(self):
        print '-------starting monitor server---------'
        self.handle()

    def process(self):
        pass

if __name__ == '__main__':
    serializer.flush_all_host_configs_into_redis()
    ms = MonitorServer('0.0.0.0','8888')
    ms.run()

