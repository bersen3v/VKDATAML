from networkx.classes import Graph
from networkx.readwrite import json_graph
from shared.datasets.methods.save_to_datasets import save_to_datasets_as_json

def save_network_x_graph(directory: str, name: str, graph: Graph):
    data = json_graph.node_link_data(graph, link='edges')
    save_to_datasets_as_json(directory=directory, name=name, data=data)
