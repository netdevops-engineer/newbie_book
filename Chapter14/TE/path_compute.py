#!/usr/bin/env python
#coding: utf-8
import sys
from ncclient import manager
import networkx as nx
from networkx.utils.misc import pairwise
import yaml
import os
from pprint import pprint

def usage():
    try:
        source = sys.argv[1]
        destination = sys.argv[2]
        prefix = sys.argv[3]
        return(source, destination, prefix)
    except IndexError:
        print("%s [source] [destination] [prefix] " %sys.argv[0])


def get_isis_topology(device):
    nc = manager.connect(**device)
    isis_xml = nc.rpc("""<get-isis-database-information>
                        <detail/>
                    </get-isis-database-information>""")
    topology = {}
    isis_entry = "//isis-database/level[text()='2']/following-sibling::*"
    for isis_database_entry in isis_xml.xpath(isis_entry):
        lsp_id = isis_database_entry.xpath("lsp-id")
        lsp_id = isis_database_entry[0].text
        lsp_id = lsp_id.replace(".00-00","")
        topology[lsp_id] = {"nodes": [], "address_prefix": []}

        for isis_neighbor in isis_database_entry.xpath("isis-neighbor"):
            isis_neighbor_id = isis_neighbor.xpath("is-neighbor-id")
            isis_neighbor_id = isis_neighbor_id[0].text
            isis_neighbor_id = isis_neighbor_id.replace(".00", "")

            isis_neighbor_metric = isis_neighbor.xpath("metric")
            isis_neighbor_metric = isis_neighbor_metric[0]
            isis_neighbor_metric = isis_neighbor_metric.text
            isis_neighbor_metric = int(isis_neighbor_metric)
            node_metric = (isis_neighbor_id, isis_neighbor_metric)
            topology[lsp_id]["nodes"].append(node_metric)

        for isis_prefix in isis_database_entry.xpath("isis-prefix"):
            address_prefix = isis_prefix.xpath("address-prefix")[0].text
            addr_metric = isis_prefix.xpath("metric")
            addr_metric = addr_metric[0].text
            addr_metric = int(addr_metric)
            prefix_metric = (address_prefix, addr_metric)
            topology[lsp_id]["address_prefix"].append(prefix_metric)


    G = nx.Graph()
    for node, infos in topology.items():
        for remote_node in infos.get("nodes"):
            G.add_edge(node, remote_node[0], weight=remote_node[1])
    return G

def load_distance_from_yamlfile(yaml_file):
    try:
        yaml_infos = yaml.load(open(yaml_file).read())
        edges = {}
        for node, edge in yaml_infos.items():
            for remote_node, weight in edge.items():
                edges[(node, remote_node)] = int(weight)
        return edges
    except FileNotFoundError:
        print("%s can't find" %yaml_file)
        sys.exit(1)

def load_loopback_from_yamlfile(yaml_file):
    try:
        nodes = yaml.load(open(yaml_file).read())
        return nodes
    except FileNotFoundError:
        print("%s can't find" %yaml_file)
        sys.exit(1)    

def load_distance(G, distance):
    for edge in G.edges:
        if distance.get((edge[0],edge[1])):

            G.edges[edge[0],edge[1]]["weight"] = distance.get((edge[0],edge[1]))
        else:
            G.edges[edge[0],edge[1]]["weight"] = distance.get((edge[1],edge[0]))
    return G

def get_route_entrys(G, source, target, prefix):
    path = nx.shortest_path(G, source, target, weight="weight")
    entrys = []
    for edge in pairwise(path):
        entrys.append({"neighbor":G.nodes[edge[0]]["loop"],"prefix": prefix, "next-hop":G.nodes[edge[1]]["loop"]})

    return entrys
 

def call_http_api(entrys, http_host="localhost"):

    for entry in entrys[::-1]:
        neighbor = entry.get("neighbor")
        prefix = entry.get("prefix")
        next_hop = entry.get("next-hop")

        exabgp_cmd = "command=neighbor %s \
                      announce route %s \
                      next-hop %s" %(neighbor, prefix, next_hop)
        cmd = 'curl --form "%s" ' %(exabgp_cmd)
        cmd = cmd + "  http://%s:5000/" %http_host
        os.system(cmd)
        

if __name__ == "__main__":
    
    argvs = usage()
    if not  argvs:
        sys.exit(1)

    isis_device = {"host": "10.0.0.4",
                   "port": 830,
                   "username": "lab",
                   "password": "lab123",
                   "hostkey_verify": False,
                   "device_params": {"name": "junos"}}

    t = get_isis_topology(isis_device)
    distance = load_distance_from_yamlfile("./distance.yaml")
    t = load_distance(t,distance)

    loop_attr = load_loopback_from_yamlfile("./devices_loopinf.yaml")
    for node in t.nodes:
        t.nodes[node]["loop"] = loop_attr[node]
    entrys = get_route_entrys(t, *argvs)
    call_http_api(entrys)
    #pprint(entrys)

