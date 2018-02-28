#!/usr/bin/env python
#coding: utf-8
import asyncio

from NetDevices import DeviceHandler

d1 = {"hostname": "vMX-1",
         "mgt_ip": "172.20.100.11",
         "username": "admin",
         "password": "lab123",
      "OS_type": "JUNOS"}

d2 = {"hostname": "vMX-2",
         "mgt_ip": "172.20.100.12",
         "username": "admin",
         "password": "lab123",
      "OS_type": "JUNOS"}

async def get_config(device):
    
    conn = DeviceHandler(device)
    conn.connect()
    await conn.login()
    r = await conn.get_config()
    print(r)

loop = asyncio.get_event_loop()

#task = loop.create_task(get_config(d))

loop.run_until_complete(asyncio.gather(get_config(d1), get_config(d2) ))
