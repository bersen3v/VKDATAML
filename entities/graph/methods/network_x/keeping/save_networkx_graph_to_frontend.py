from networkx.classes import Graph
from networkx.readwrite import json_graph
from shared.datasets.methods.save_to_datasets import save_to_datasets_as_json


def save_networkx_graph_to_frontend(graph: Graph, directory: str, name: str):
    data = json_graph.node_link_data(graph, link='edges')
    frontend_graph = {"nodes": data['nodes'], "links": data['edges']}
    save_to_datasets_as_json(directory=directory, name=name, data=frontend_graph)
