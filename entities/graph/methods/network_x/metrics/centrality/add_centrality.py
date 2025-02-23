import networkx as nx
from networkx.classes import Graph


def add_centrality(graph: Graph) -> Graph:
    centrality = nx.degree_centrality(graph)

    for node, cent in centrality.items():
        graph.nodes[node]['centrality'] = cent

    return graph