import networkx as nx
from networkx.classes import Graph


def add_page_rank(graph: Graph) -> Graph:
    pagerank = nx.pagerank(graph)

    for node, cent in pagerank.items():
        graph.nodes[node]['pagerank'] = cent

    return graph