#!/usr/bin/python
import sys

args = sys.argv

if len(args)==1:
    print("please input destination IP address")

elif len(args)>1:
    for arg in args[1:]:
        print("Let's test the host, IP is %s" %arg)


