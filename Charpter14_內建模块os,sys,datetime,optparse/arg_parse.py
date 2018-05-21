#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

def qyt_argparse(filename, iface):
    print(filename)
    print(iface)


if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = "usage: python testargparse.py -f filename -i interface"

    parser = ArgumentParser(usage=usage)

    parser.add_argument("-f", "--file", dest="filename", help="Write report to FILE", default='defaultFilename', type= str)
    parser.add_argument("-i", "--interface", dest="iface", help="Specify an interface", default=1, type= int)
    parser.add_argument(nargs='?', dest="host", help="Specify an host", default='10.1.1.1', type=str)
    #parser.add_argument(nargs='*', dest="hosts", help="Specify an host", default='10.1.1.1', type=str)
    args = parser.parse_args()

    print(args.host)
    #print(args.hosts)
    qyt_argparse(args.filename, args.iface)