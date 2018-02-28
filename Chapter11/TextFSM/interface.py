#!/usr/bin/env python
#coding: utf-8

import textfsm

TEMP_FILE = "interface_template"
INPUT_FILE = "interface.cfg"

fsm = textfsm.TextFSM(open(TEMP_FILE))
input_txt = open(INPUT_FILE).read()

fsm_results = fsm.ParseText(input_txt)

print(fsm.header)
for row in fsm_results:
    print(row)
