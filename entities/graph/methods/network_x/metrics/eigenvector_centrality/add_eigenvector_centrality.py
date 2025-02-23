import networkx as nx
from networkx.classes import Graph


def add_eigenvector_centrality(graph: Graph) -> Graph:
    eigenvector_centrality = nx.eigenvector_centrality(graph)

    for node, cent in eigenvector_centrality.items():
        graph.nodes[node]['eigenvector_centrality'] = cent

    return graph