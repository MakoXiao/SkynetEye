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
@file: cpu.py
@time: 2015-11-28 下午1:51
"""
import time

def monitor(frist_invoke=1):

        interval=2

        f = open('/proc/stat')
        cpu_t1 = f.readline().split()
        f.close()

        time.sleep(interval)

        f = open('/proc/stat')
        cpu_t2 = f.readline().split()
        f.close()

        cpu_total_t1 = float(eval(('+'.join(cpu_t1)).split('cpu+')[1]))
        cpu_idle_t1 = float(cpu_t1[4])


        cpu_total_t2 = float(eval(('+'.join(cpu_t2)).split('cpu+')[1]))
        cpu_idle_t2 = float(cpu_t2[4])

        cpu_idle = cpu_idle_t2-cpu_idle_t1
        cpu_total = cpu_total_t2-cpu_total_t1

        cpu_percent = (cpu_total-cpu_idle)/cpu_total

        value_dic = {
            'cpu.user': float(cpu_t1[1])/cpu_total_t1*100,
            'cpu.nice':float(cpu_t1[2])/cpu_total_t1*100,
            'cpu.system':float(cpu_t1[3])/cpu_total_t1*100,
            'cpu.idle':float(cpu_t1[4])/cpu_total_t1*100,
            'cpu.iowait': float(cpu_t1[5])/cpu_total_t1*100,
            'cpu.irq': float(cpu_t1[6])/cpu_total_t1*100,
            'cpu.softirq': float(cpu_t1[7])/cpu_total_t1*100,
            'cpu.stealstolen':float(cpu_t1[8])/cpu_total_t1*100,
            'cpu.guest': float(cpu_t1[9])/cpu_total_t1*100,
            'cpu.percent': cpu_percent*100
        }

        return value_dic

if __name__ == '__main__':
    print monitor()