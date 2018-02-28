#!/usr/bin/env python
#coding:utf-8
from ciscoconfparse import CiscoConfParse, IOSCfgLine
cfg = open("isis_ios.cfg").read().splitlines()

parse = CiscoConfParse(cfg)

Eth_re = "interface\s+\w+Ethernet"
for obj in parse.find_objects_wo_child(Eth_re, "point-to-point"):
    obj.insert_after("  point-to-point")


for line in parse.ioscfg:
    print(line)



