import networkx as nx
from networkx.classes import Graph

def add_degree(graph: Graph) -> Graph:
    for node in graph.nodes:
        node_degree = graph.degree[node]
        graph.nodes[node]['degree'] = node_degree
    return graph
