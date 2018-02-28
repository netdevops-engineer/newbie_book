#!/usr/bin/env python
#coding:utf-8
import networkx as nx

nodes = ["BJ", "SH", "GZ", "HZ","NJ","WH","XA"]
G = nx.Graph()
for node in nodes:
    G.add_node(node)

edges = [("BJ", "SH"),
         ("BJ", "GZ"),
         ("SH", "GZ"),
         ]

