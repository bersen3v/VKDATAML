import asyncio
import json

import networkx as nx
from networkx.classes import Graph
from networkx.readwrite import json_graph

from entities.graph.methods.create_graph import create_graph
from entities.graph.methods.network_x.keeping.save_networkx_graph_to_frontend import save_networkx_graph_to_frontend
from entities.graph.methods.network_x.metrics.add_metrics.add_metrics import add_metrics
from entities.graph.methods.network_x.keeping.save_network_x_graph import save_network_x_graph
from entities.user.api.constants.user_fields import primary_fields
from entities.user.methods.friends_binary_search import friends_binary_search
from entities.user.methods.get_friends_list import get_friends_list
from entities.user.methods.get_user_model_by_id import get_user_model_by_id
from entities.user.model.user import User
from shared.db.DBController import db_controller

def get_networkx_graph_as_json(graph: Graph):
    data = json_graph.node_link_data(graph, link='edges')
    frontend_graph = {"nodes": data['nodes'], "links": data['edges']}
    return frontend_graph

def create_graph_async(customer_id: str, object_id: int | str, users_list: list[User], count: int = 5000):
    saved = False
    graph = nx.Graph()
    prev_graph = graph
    process = 0
    for user in users_list:
        process+=1

        if process >= 5 and not saved:
            json_graph_1 = get_networkx_graph_as_json(graph)
            asyncio.run(db_controller.add_graph_to_history(customer_id, json_graph_1))
            saved = True

        print(f"{process} / {len(users_list)}")
        graph = add_user_to_graph_async(graph=graph, user=user ,users_list=users_list, count=count)
        # if not graph.add_edge(user.id, user_friend.id):
        #     graph.add_edge(user.id, user_friend.id)
        diff_graph = nx.difference(graph, prev_graph)
        prev_graph = graph
        json_graph = get_networkx_graph_as_json(graph)
        yield json.dumps(json_graph)

    # graph = add_metrics(graph)
    # save_networkx_graph_to_frontend(graph=graph, directory=str(object_id), name = "frontend_graph")
    # save_network_x_graph(graph=graph, directory=str(object_id), name = "networkx_graph" )
    #
    # return graph

def add_user_to_graph_async(graph: Graph, user: User,  users_list: list[User], count: int = 5000):
    if not graph.has_node(user.id):
        graph.add_node(user.id, id = f"{user.id}", name=f"{user.first_name} {user.last_name}", bdate = user.bdate, city = user.city.title if user.city is not None else None, home_town = user.home_town, sex = user.sex, img = f"{user.photo_max_orig}")
    if not user.is_closed:
        user_friends = get_friends_list(user.id, count=count, query_fields=primary_fields)
        for user_friend in user_friends:
            friend_index = friends_binary_search(user_friend, users_list)
            if friend_index != -1:
                if not graph.has_node(user_friend.id):
                    graph.add_node(user_friend.id, id=f"{user_friend.id}",
                                   name=f"{user_friend.first_name} {user_friend.last_name}", bdate=user_friend.bdate,
                                   city=user_friend.city.title if user_friend.city is not None else None,
                                   home_town=user_friend.home_town,
                                   sex=user_friend.sex, img=f"{user_friend.photo_max_orig}")
                if not graph.add_edge(user.id, user_friend.id):
                    graph.add_edge(user.id, user_friend.id)
    return graph

