#!/usr/bin/env python
#coding:utf-8
from ciscoconfparse import CiscoConfParse, IOSCfgLine
cfg = open("isis_junos.cfg").read().splitlines()

parse = CiscoConfParse(cfg,syntax='junos', comment='#!')

print("\n".join(parse.ioscfg))

print("Check interface without 'point-to-point' config line:")
for obj in parse.find_objects_wo_child("interface", "point-to-point"):
    print(obj.text)

