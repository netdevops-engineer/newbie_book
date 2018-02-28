#!/usr/bin/env python
#coding:utf-8

cfg = open("isis_set.cfg").read().splitlines()

for line in cfg:
    if "point-to-point" in line:
        line_list = line.split()
        print(line_list[4])
