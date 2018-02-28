#!/usr/bin/python
bgp_peers = ["10.1.1.100", "10.1.1.101", "10.1.1.102", "10.1.1.103"]

print("router bgp 100")

for peer in bgp_peers:
    print("neighbor %s remote-as 100" %peer)
    print("neighbor %s update-source lo0" %peer)

print("exit")
