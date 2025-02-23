from networkx.classes import Graph

from entities.graph.methods.network_x.communities.get_communities import get_communities

def add_communities_to_graph(graph: Graph):
    communities = get_communities(graph=graph)
    for community_index in range(len(communities)):
        for user_id in communities[community_index]:
            graph.nodes[user_id]['community'] = community_index
    return graph

