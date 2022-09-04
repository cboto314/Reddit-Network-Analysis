import networkx as nx
import pandas as pd

G = nx.read_gexf('bellingcat.gexf')

#edges_df = pd.DataFrame(G.edges)
#redditors = [x[0] for x in G.nodes if x[1]==1 ]

#edges_df = edges_df.drop(edges_df[0] not in redditors)