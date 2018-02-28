#!/usr/bin/env python
#coding:utf-8
from ciscoconfparse import CiscoConfParse
cfg = open("isis_ios.cfg").read().splitlines()

parse = CiscoConfParse(cfg)

for obj in parse.find_objects(r"interface"):
     #print(obj.text)
     if obj.re_search_children(r"point-to-point"):
        print(obj.text)
