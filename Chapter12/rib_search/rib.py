#!/usr/bin/env python
#coding: utf-8

import textfsm
from netaddr import *
import time


TEMP_FILE = "rib_tmplate"
INPUT_FILE = "internet_rib.txt"

fsm = textfsm.TextFSM(open(TEMP_FILE))
input_txt = open(INPUT_FILE).read()

Start_time = time.time()
print("Start to Parse %s file, The Start time is %s" %(INPUT_FILE,Start_time))
fsm_results = fsm.ParseText(input_txt)
print("Stop Parse file, elapsed time is %f" % (time.time() - Start_time))

def get_prefixlen(prefix):
    first_byte = prefix.split(".")[0]
    first_byte = int(first_byte)
    ip_network = cidr_abbrev_to_verbose(first_byte)
    _, prefixlen = ip_network.split("/")

    return prefixlen


Start_time = time.time()
ip_list = []
for ip in fsm_results:
    ip = ip[0]
    if "/" not in ip:
        ip_list.append(IPNetwork(ip +"/" + get_prefixlen(ip)))
    else:
        ip_list.append(IPNetwork(ip))
print("load rib finish elapsed time is %f" %(time.time() - Start_time)) 

ip_address = IPNetwork("202.97.32.1")
Start_time = time.time()
ip_address_supernets = ip_address.supernet(8)
for ip in ip_address_supernets[::-1]:
    if ip in ip_list:
        print(ip)
        break
print("Search time is %s" %(time.time() - Start_time))


 
