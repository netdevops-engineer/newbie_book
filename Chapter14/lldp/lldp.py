#!/usr/bin/env python
#coding: utf-8
import asyncio
import yaml
import sys
from NetDevices import DeviceHandler
import textfsm

def parser_lldp(device, lldp_result):
    OS_type = device.get("OS_type")
    tmp_file = "./textfsm_tmp/lldp/%s.tmp" %OS_type
    fsm = textfsm.TextFSM(open(tmp_file))
    fsm_results = fsm.ParseText(lldp_result)
    return fsm_results

async def get_lldp(device):
    conn = DeviceHandler(device)
    conn.connect()
    await conn.login()
    r = await conn.get_lldp()
    lldp_lists = parser_lldp(device, r[1])
    print(lldp_lists)

deviceinfos = {}
try:
   yaml_cfg = sys.argv[1]
#   f =  open(yaml_cfg)
#   deviceinfos = yaml.load(f.read())

except IndexError:
   print("please give yaml configure file")
   sys.exit(1)

f =  open(yaml_cfg)
deviceinfos = yaml.load(f.read())


loop = asyncio.get_event_loop()
tasks = []
for device in deviceinfos.get("devices"):
    tasks.append(loop.create_task(get_lldp(device)))

loop.run_until_complete(asyncio.wait(tasks))

