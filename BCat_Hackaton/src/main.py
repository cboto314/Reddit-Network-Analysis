from pmaw import PushshiftAPI
import argparse
from datetime import datetime
from prawcore.exceptions import Forbidden
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

import helpers.fetch as sc


api = PushshiftAPI(base_backoff="jitter")
parser = argparse.ArgumentParser("Reddit Network Analysis Tool")

#DB Paths
path_to_user_details = "users.csv"
path_to_sub_details = "sub.csv"
path_to_network = "nodes_edges.csv"

parser.add_argument("--root", 
                    dest='root_node',
                    type=str,
                    help="Specifies the root node",
                    required = True)
parser.add_argument("--type", 
                    dest='node_type' ,
                    type=int,
                    help="Specifies type of node (1 = user, 2 = subreddit)",
                    choices=range(1,3),
                    required = True)
parser.add_argument("--export", 
                    dest='export' ,
                    type=bool,
                    help="Save intermediate scraping results to csv. Default=False",
                    choices=[True,False],
                    default=False,
                    required = False)

args = parser.parse_args()

root_node = (args.root_node, args.node_type)
export = args.export

depth = 2 # How many iterations
max_edges = 1 # How many edges a node can have
queue_thresh = 5
scrape_limit = 100
network = []

network = sc.get_nodes(api,root_node,depth,max_edges,scrape_limit,export)

G = nx.Graph()
for node in network:
    nodeA = (node[0],{"type":node[1]})
    nodeB = (node[2],{"type":node[3]})
    G.add_nodes_from([
        nodeA,
        nodeB,
    ])
    G.add_edge(nodeA[0],nodeB[0],weight=node[4])

nx.write_gexf(G, "reddit.gexf")