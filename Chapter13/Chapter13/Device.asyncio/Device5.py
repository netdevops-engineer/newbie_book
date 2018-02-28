#!/usr/bin/env python
#coding: utf-8
import asyncio
import yaml
import sys
from NetDevices import DeviceHandler

async def get_config(device):
    conn = DeviceHandler(device)
    conn.connect()
    await conn.login()
    r = await conn.get_config()
    for line in r[1].split("\r\n"):
        print(line)


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

print(deviceinfos)

loop = asyncio.get_event_loop()
tasks = []
for device in deviceinfos.get("devices"):
    tasks.append(loop.create_task(get_config(device)))

loop.run_until_complete(asyncio.wait(tasks))
