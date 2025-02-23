import networkx as nx
from networkx.classes import Graph

from entities.graph.methods.network_x.keeping.save_networkx_graph_to_frontend import save_networkx_graph_to_frontend
from entities.graph.methods.network_x.metrics.add_metrics.add_metrics import add_metrics
from entities.graph.methods.network_x.keeping.save_network_x_graph import save_network_x_graph
from entities.user.api.constants.user_fields import primary_fields
from entities.user.methods.friends_binary_search import friends_binary_search
from entities.user.methods.get_friends_list import get_friends_list
from entities.user.model.user import User

def create_graph(object_id: int|str, users_list: list[User], count: int = 5000):
    graph = nx.Graph()

    process = 0
    for user in users_list:
        process+=1
        print(f"{process} / {len(users_list)}")
        graph = add_user_to_graph(graph=graph, user=user ,users_list=users_list, count=count)

    graph = add_metrics(graph)
    save_networkx_graph_to_frontend(graph=graph, directory=str(object_id), name = "frontend_graph")
    save_network_x_graph(graph=graph, directory=str(object_id), name = "networkx_graph" )

    return graph

def add_user_to_graph(graph: Graph, user: User,  users_list: list[User], count: int = 5000):
    graph.add_node(user.id, id = f"{user.id}", name=f"{user.first_name} {user.last_name}", bdate = user.bdate, city = user.city.title if user.city is not None else None, home_town = user.home_town, sex = user.sex, img = f"{user.photo_max_orig}")
    if not user.is_closed:
        user_friends = get_friends_list(user.id, count=count, query_fields=primary_fields)
        for user_friend in user_friends:
            friend_index = friends_binary_search(user_friend, users_list)
            if friend_index != -1:
                graph.add_edge(user.id, user_friend.id)
    return graph

