import json
import networkx as nx
from networkx.classes import Graph

def get_graph_from_json(directory: str) -> Graph:
    with open(f'shared/datasets/data/{directory}/networkx_graph.json', 'r') as file:
        data = json.load(file)
    graph = nx.node_link_graph(data, link="edges")
    return graph