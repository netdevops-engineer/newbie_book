# coding:utf-8
#!/usr/bin/env python

from ncclient import manager

device = {"host": "172.20.1.11",
          "port": 830,
          "username": "lab",
          "password": "lab123",
          "hostkey_verify": False,
          "device_params": {'name':'junos'}}
nc = manager.connect(**device)

interfaces = nc.rpc("<get-interface-information/>")

print(interfaces.xpath('//physical-interface/name').text)