#!/usr/bin/env python
#coding: utf-8
import asyncio
import yaml
import sys
from NetDevices import DeviceHandler
from git import Repo
import time


FILEPATH = "/root/device_cfg/"
async def get_config(device):
    hostname = device.get("hostname")
    conn = DeviceHandler(device)
    conn.connect()
    await conn.login()
    r = await conn.get_config()
    file_name = FILEPATH + hostname
    open(file_name, "w").write(r[1]) 
    print("%s is saved" %file_name)

deviceinfos = {}
try:
   yaml_cfg = sys.argv[1]

except IndexError:
   print("please give yaml configure file")
   sys.exit(1)

f =  open(yaml_cfg)
deviceinfos = yaml.load(f.read())


loop = asyncio.get_event_loop()
tasks = []
for device in deviceinfos.get("devices"):
    tasks.append(loop.create_task(get_config(device)))

loop.run_until_complete(asyncio.wait(tasks))
localtime = time.asctime(time.localtime(time.time()))
repo = Repo(FILEPATH)
repo.index.add("*")
repo.index.commit("Configs auto saving at %s" %localtime)

