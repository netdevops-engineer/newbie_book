#!/usr/bin/python

protocol = input("Please input protocol name: ")
protocol = protocol.lower()

if protocol == "tcp":
    print("TCP's protocol id is 6 ")

elif protocol == "udp":
    print("UDP's protocol id is 17 ")
else:
    print("UNKOWN protocol")

