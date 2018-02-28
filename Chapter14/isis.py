#!/usr/bin/env python
from pprint import pprint
from ncclient import manager
import networkx as nx

device = {"host": "10.0.0.4",
           "port": 830,
           "username": "lab",
           "password": "lab123",
           "hostkey_verify": False,
            "device_params": {"name": "junos"}}

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


G = nx.DiGraph()

for node, infos in topology.items():
    for remote_node in infos.get("nodes"):
        G.add_edge(node, remote_node[0], weight=remote_node[1])


nodes = G.nodes

def get_local_prefix(node):
    prefixs = []
    for prefix in topology[node]["address_prefix"]:
        prefixs.append(prefix[0])
    return prefixs
for node in nodes:
    print("router %s 's route tables:"%node)
    print("%-18s %-7s %-7s" %("prefix","nexthop","metric"))
    print("-"*30)
    for remote_node in nodes:
        if remote_node == node:
            for prefix in topology.get(node).get("address_prefix"):
                print("%-18s %-7s %-7s" %(prefix[0], "Local", prefix[1]))
        else:
            path = nx.dijkstra_path(G,node, remote_node, weight="weight")
            path_length = nx.dijkstra_path_length(G, node, remote_node, weight="weight")
            
            for prefix in topology.get(remote_node).get("address_prefix"):
                if prefix[0] not in get_local_prefix(node):
                    print("%-18s %-7s %-7s" %(prefix[0], path[1],path_length +prefix[1])) 
    print("="*30)
