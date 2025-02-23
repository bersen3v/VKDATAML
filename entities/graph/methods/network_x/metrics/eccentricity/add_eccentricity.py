import networkx as nx
from networkx.classes import Graph


def add_eccentricity(graph: Graph) -> Graph:
    eccentricity = nx.eccentricity(graph)
    for node, cent in eccentricity.items():
        graph.nodes[node]['eccentricity'] = cent
    return graph