#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from module import qyt_multi
from multiprocessing import Pool as ProcessPool
from multiprocessing.pool import ThreadPool
from multiprocessing import freeze_support
import random

#多进程
#freeze_support()  # Windows 平台要加上这句，避免 RuntimeError
pool = ProcessPool(processes=5)#有效控制并发进程或者线程数，不设置为内核数(推荐)
#cpus = multiprocessing.cpu_count()#得到内核数的方法

#多线程
#pool = ThreadPool(processes=5)

results = []
for i in range(0, 10):
    x = random.randint(1,10)
    y = random.randint(1,10)
    z = random.randint(1,10)
    result = pool.apply_async(qyt_multi, args=(x,y,z))
    results.append(result)

pool.close()
pool.join()#调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束

for i in results:
    print(i.get())