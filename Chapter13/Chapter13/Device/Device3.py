#!/usr/bin/env python
#coding: utf-8

from NetDevices import DeviceHandler

d = {"hostname": "vMX-1",
         "mgt_ip": "172.20.100.11",
         "username": "admin",
         "password": "lab123",
      "OS_type": "JUNOS"}

conn = DeviceHandler(d)
conn.connect()
r = conn.login()
print(conn.get_config())
