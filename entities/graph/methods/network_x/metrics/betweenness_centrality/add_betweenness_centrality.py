import networkx as nx
from networkx.classes import Graph


def add_betweenness_centrality(graph: Graph) -> Graph:
    betweenness_centrality = nx.betweenness_centrality(graph)

    for node, cent in betweenness_centrality.items():
        graph.nodes[node]['betweenness_centrality'] = cent

    return graph