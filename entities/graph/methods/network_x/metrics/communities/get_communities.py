import networkx as nx
from networkx.classes import Graph

def get_communities(graph: Graph):
    partition = nx.community.louvain_communities(graph, seed=123)
    return partition

