import json
import pandas as pd

from entities.graph.methods.create_graph import create_graph
from entities.graph.methods.network_x.metrics.betweenness_centrality.add_betweenness_centrality import \
    add_betweenness_centrality
from entities.graph.methods.network_x.metrics.centrality.add_centrality import add_centrality
from entities.graph.methods.network_x.keeping.get_graph_from_json import get_graph_from_json
from entities.graph.methods.network_x.keeping.save_network_x_graph import save_network_x_graph
from entities.graph.methods.network_x.metrics.closeness_centrality.add_closeness_centrality import \
    add_closeness_centrality
from entities.graph.methods.network_x.metrics.degree.add_degree import add_degree
from entities.graph.methods.network_x.metrics.eccentricity.add_eccentricity import add_eccentricity
from entities.graph.methods.network_x.metrics.eigenvector_centrality.add_eigenvector_centrality import \
    add_eigenvector_centrality
from entities.graph.methods.network_x.metrics.page_rank.add_page_rank import add_page_rank
from entities.group.methods.get_group_model_by_id import get_group_model_by_id
from entities.group.methods.get_subscribers_list import get_subscribers_list
from entities.group.methods.get_user_graph import get_user_graph
from entities.group.model.group import Group
from entities.user.api.get_users_by_id import get_users_by_id
from entities.user.methods.get_friends_list import get_friends_list
from entities.user.methods.get_user_model_by_id import get_user_model_by_id
from shared.constants import vk_api_token

# file = open('shared/datasets/data/data_116131349/networkx_graph.json')
# data = json.loads(file.read())['nodes']
# df = pd.DataFrame(data=data)
# df.to_csv("ikit.csv")

get_user_graph('303561841')

# group_data = get_groups_by_id(access_token=vk_api_token, group_ids=['ikitinfo'])
# group = Group.from_json(group_data['data']['response']['groups'][0])
# subscribers = []
# for i in range(5):
#     subscribers += get_subscribers_list(group_id=group.id, offset=1000*i)
# create_graph(object_id=group.id, users_list=subscribers)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time)
# user = User.from_json(get_user_by_id(access_token=vk_api_token))

# group = get_by_id(id = "ikitinfo")
# subscribers = []
# for i in range(5):
#     subscribers += get_subscribers_list(group_id=group.id, offset=1000*i)
# create_graph(object_id=group.id, users_list=subscribers, count = 1000)


