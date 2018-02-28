#!/usr/bin/env python
from netaddr import IPNetwork

inf_cfg = '''
interface GigabitEthernet0/0/0/1.%d
 ipv4 address %s 255.255.255.252
 encapsulation dot1q %d
!
'''

ip_net = IPNetwork("172.20.1.1/24")
for i in range(1, 11):
    ip = ip_net.ip + (i - 1) *4
    print(inf_cfg %(i, ip, i))
