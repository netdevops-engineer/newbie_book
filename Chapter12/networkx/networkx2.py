#!/usr/bin/env python
#coding:utf-8
import networkx as nx

nodes = ["BJ", "SH", "GZ", "HZ","NJ","WH","XA"]
G = nx.Graph()
for node in nodes:
    G.add_node(node)

edges = [("BJ", "SH",1200),
         ("BJ", "GZ",2500),
         ("SH", "GZ",1300),
         ("HZ", "SH",280),
         ("HZ", "GZ",1000),
         ("NJ", "SH",300),
         ("NJ", "BJ",900),
         ("WH", "SH",800),
         ("WH", "BJ",850),
         ("XA", "GZ",2600),
         ("XA", "BJ",2000),]
G.add_weighted_edges_from(edges)


