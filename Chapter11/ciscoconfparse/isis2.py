#!/usr/bin/env python
#coding:utf-8
from ciscoconfparse import CiscoConfParse
cfg = open("isis_ios.cfg").read().splitlines()

parse = CiscoConfParse(cfg)

for obj in parse.find_objects(r"interface"):
    af_v4 = obj.re_search_children(r"address-family ipv4")
    for metric in af_v4:
        if metric.re_search_children(r"metric 20"):
            print(obj.text)
