#!/usr/bin/env python
#coding:utf-8
import re
cfg = open("isis_set.cfg").read().splitlines()
interfaces = set()
p2p_infs = set()
interface_re = r"[x|g|e][e|t]\-\d+\/\d+\/\d+\.\d+"
for line in cfg:
    line_split = line.split()
    if len(line_split) > 5:
        if re.match(interface_re, line_split[4]):
            interfaces.add(line_split[4])
        print(line_split)
        if "point-to-point" == line_split[5]:
            p2p_infs.add(line_split[4])

no_p2p_infs = interfaces - p2p_infs
for inf in no_p2p_infs:
    inf_cfg = "set protocols isis interface %s point-to-point" %inf
    cfg.append(inf_cfg)

print("\n".join(cfg))
