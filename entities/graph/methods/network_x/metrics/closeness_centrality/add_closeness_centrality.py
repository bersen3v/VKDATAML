import networkx as nx
from networkx.classes import Graph


def add_closeness_centrality(graph: Graph) -> Graph:
    closeness_centrality = nx.closeness_centrality(graph)

    for node, cent in closeness_centrality.items():
        graph.nodes[node]['closeness_centrality'] = cent

    return graph