from networkx.classes import Graph

from entities.graph.methods.network_x.metrics.betweenness_centrality.add_betweenness_centrality import \
    add_betweenness_centrality
from entities.graph.methods.network_x.metrics.centrality.add_centrality import add_centrality
from entities.graph.methods.network_x.metrics.closeness_centrality.add_closeness_centrality import \
    add_closeness_centrality
from entities.graph.methods.network_x.metrics.communities.add_communities_to_graph import add_communities_to_graph
from entities.graph.methods.network_x.metrics.degree.add_degree import add_degree
from entities.graph.methods.network_x.metrics.eigenvector_centrality.add_eigenvector_centrality import \
    add_eigenvector_centrality
from entities.graph.methods.network_x.metrics.page_rank.add_page_rank import add_page_rank


def add_metrics(graph: Graph)-> Graph:

    graph = add_communities_to_graph(graph=graph)
    print("communities")

    graph = add_degree(graph)
    print("degree")

    graph = add_centrality(graph)
    print("centrality")

    graph = add_betweenness_centrality(graph)
    print("betweenness_centrality")

    graph = add_closeness_centrality(graph)
    print("closeness_centrality")

    graph = add_eigenvector_centrality(graph)
    print("eigenvector_centrality")

    graph = add_page_rank(graph)
    print("page_rank")
    return  graph