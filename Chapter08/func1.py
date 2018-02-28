#!/usr/bin/python
def ipv4_to_int(ipv4):
    ipv4 = [int(x) for x in ipv4.split(".")]
    ipv4_int = (ipv4[0] << 24) + (ipv4[1] << 16) + (ipv4[2] << 8) + ipv4[3]
    return ipv4_int

def int_to_ipv4(ip_int):
    ipv4 = []
    for x in (24, 16, 8 ,0):
        ipv4.append(str(ip_int >> x & 0xFF))
    return ".".join(ipv4) 


    
print(int_to_ipv4(ipv4_to_int("1.1.1.2")))
