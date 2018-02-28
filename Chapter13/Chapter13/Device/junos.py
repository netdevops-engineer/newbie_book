#!/usr/bin/env python
#coding:utf-8
from NetDevices import JUNOS
d = {"hostname": "vMX-1",
         "mgt_ip": "172.20.100.11",
         "username": "admin",
         "password": "lab123"}
conn = JUNOS(d)
conn.connect()
conn.login()
print(conn.get_config())
