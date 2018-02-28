#!/usr/bin/env python
#coding:utf-8
from ciscoconfparse import CiscoConfParse
cfg = open("isis_ios.cfg").read().splitlines()

parse = CiscoConfParse(cfg)

required_lines = [
                 "address-family ipv4 unicast",
                 "point-to-point",
                 ]

for obj in parse.find_objects(r"interface"):
    p = CiscoConfParse(obj.ioscfg)
    result = p.req_cfgspec_all_diff(required_lines)
    if result:
        print(obj.text)
        print("missing config line(s):")
        print("\n".join(result))
        print("="*20)
